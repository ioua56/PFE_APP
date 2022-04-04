import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import './index.css';
import { Button, Input, Header } from '../../../../ui/src/components';
const Login = () => {
  return (
    <div>
      <Header isReturnEnabled={false} menuOptions={[]}></Header>
      <div className="auth-wrapper ">
        <div className="auth-inner ">
          <form>
            <h3>Sign In</h3>

            <div className="form-group">
              <Input
                label={'Email'}
                type="email"
                className="form-control"
                placeholder="Enter email"
              />
            </div>

            <div className="form-group">
              <Input
                label={'Password'}
                type="password"
                className="form-control"
                placeholder="Enter password"
              />
            </div>

            <div className="form-group">
              <div className="custom-control custom-checkbox">
                <input
                  label={'Remember me'}
                  type="checkbox"
                  className="custom-control-input"
                  id="customCheck1"
                />
                <label className="custom-control-label" htmlFor="customCheck1">
                  Remember me
                </label>
              </div>
            </div>

            <Button type="submit" className="btn-block">
              Submit
            </Button>
            <p className="forgot-password text-right">
              Forgot <a href="/singup">password?</a>
            </p>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;
