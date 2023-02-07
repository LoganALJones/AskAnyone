import React, { useState } from 'react';
import { cookies } from 'next/headers';

const CookieCheck = () => {
  const [visited, setVisited] = useState(false);
  const nextCookies = cookies();

  if (!visited && nextCookies.has('visited')) {
    setVisited(true);
  }

  return visited;
};

export default CookieCheck;
