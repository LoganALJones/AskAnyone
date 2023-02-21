import { initializeApp } from "firebase/app";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
  apiKey: "AIzaSyDDNDVtpEETYf_mIL3TigKNB21s8Ml8Hmo",
  authDomain: "askanyone-d733c.firebaseapp.com",
  projectId: "askanyone-d733c",
  storageBucket: "askanyone-d733c.appspot.com",
  messagingSenderId: "637371372437",
  appId: "1:637371372437:web:373d15ab2e8dd322a75c9c",
  measurementId: "G-76DWKGQF1J"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const storage = getStorage(app);