import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { ErrorBoundary } from '@ohif/ui';
import 'bootstrap/dist/css/bootstrap.min.css';

// Route Components
import DataSourceWrapper from './DataSourceWrapper';
import WorkList from './WorkList';
import Local from './Local';
import NotFound from './NotFound';
import buildModeRoutes from './buildModeRoutes';
import PrivateRoute from './PrivateRoute';
import Login from './Login';
import Singup from './Singup';
import PatientList from './PatientList';

// TODO: Make these configurable
// TODO: Include "routes" debug route if dev build
const bakedInRoutes = [
  {
    path: '/stdlist',
    children: DataSourceWrapper,
    private: true,
    props: { children: WorkList },
  },
  {
    path: '/patientlist',
    children: DataSourceWrapper,
    props: { children: PatientList },
  },
  {
    path: '/local',
    children: Local,
  },
  // NOT FOUND (404)
  { path: '*', children: NotFound },
  { path: '/', children: Login },
  { path: 'login', children: Login },
  { path: 'singup', children: Singup },
];

const createRoutes = ({
  modes,
  dataSources,
  extensionManager,
  servicesManager,
  hotkeysManager,
  routerBasename,
}) => {
  const routes =
    buildModeRoutes({
      modes,
      dataSources,
      extensionManager,
      servicesManager,
      hotkeysManager,
    }) || [];

  const allRoutes = [...routes, ...bakedInRoutes];

  function RouteWithErrorBoundary({ route, ...rest }) {
    // eslint-disable-next-line react/jsx-props-no-spreading
    return (
      <ErrorBoundary context={`Route ${route.path}`} fallbackRoute="/">
        <route.children
          {...rest}
          {...route.props}
          route={route}
          servicesManager={servicesManager}
          hotkeysManager={hotkeysManager}
        />
      </ErrorBoundary>
    );
  }

  const { UserAuthenticationService } = servicesManager.services;

  return (
    <Routes basename={routerBasename}>
      {allRoutes.map((route, i) => {
        console.log(route);
        return route.private === true ? (
          <PrivateRoute
            key={i}
            path={route.path}
            handleUnauthenticated={
              UserAuthenticationService.handleUnauthenticated
            }
            element={<RouteWithErrorBoundary route={route} />}
          />
        ) : (
          <Route
            key={i}
            path={route.path}
            element={<RouteWithErrorBoundary route={route} />}
          />
        );
      })}
    </Routes>
  );
};

export default createRoutes;
