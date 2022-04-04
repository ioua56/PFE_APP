import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import './index.css';
import { Button, Header, Input } from '../../../../ui/src/components';

const Singup = () => {
  const menuOptions = [];
  return (
    <div>
      <Header isReturnEnabled={false} menuOptions={menuOptions}></Header>
      <div className="auth-wrapper">
        <div className="auth-inner">
          <form>
            <h3>Sign Up</h3>

            <div className="form-group">
              <label>First name</label>
              <Input
                type="text"
                className="form-control"
                placeholder="First name"
              />
            </div>

            <div className="form-group">
              <label>Last name</label>
              <Input
                type="text"
                className="form-control"
                placeholder="Last name"
              />
            </div>

            <div className="form-group">
              <label>Email address</label>
              <Input
                type="email"
                className="form-control"
                placeholder="Enter email"
              />
            </div>

            <div className="form-group">
              <label>Password</label>
              <Input
                type="password"
                className="form-control"
                placeholder="Enter password"
              />
            </div>

            <Button type="submit" className="btn-block">
              Sign Up
            </Button>
            <p className="forgot-password text-right">
              Already registered <a href="/login">sign in?</a>
            </p>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Singup;
