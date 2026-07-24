import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import SearchBox from './components/SearchBox';
import Statistics from './components/Statistics';
import Features from './components/Features';
import HowItWorks from './components/HowItWorks';
import TopHospitals from './components/TopHospitals';
import FeaturedJobs from './components/FeaturedJobs';
import EmployerSection from './components/EmployerSection';
import Testimonials from './components/Testimonials';
import FAQ from './components/FAQ';
import CTA from './components/CTA';
import Footer from './components/Footer';

function App() {
  return (
    <div className="min-h-screen overflow-x-hidden">
      <Navbar />
      <main>
        <Hero />
        <SearchBox />
        <Statistics />
        <Features />
        <HowItWorks />
        <TopHospitals />
        <FeaturedJobs />
        <EmployerSection />
        <Testimonials />
        <FAQ />
        <CTA />
      </main>
      <Footer />
    </div>
  );
}

export default App;
