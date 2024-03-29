import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

const NotFound = ({
  message = 'Sorry, this page does not exist.',
  showGoBackButton = true,
}) => {
  return (
    <div className="bg-black w-full h-full flex justify-center items-center text-white">
      <div>
        <h1>{message}</h1>
        {showGoBackButton && (
          <h5>
            <Link to={'/'}>Go back to the Study List</Link>
          </h5>
        )}
      </div>
    </div>
  );
};

NotFound.propTypes = {
  message: PropTypes.string,
  showGoBackButton: PropTypes.bool,
};

export default NotFound;
