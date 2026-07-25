import React from 'react';
import { motion } from 'framer-motion';

const jobs = [
    { title: 'Senior Cardiologist', hospital: 'Apollo Hospitals', location: 'Mumbai, MH', salary: '₹2.5L – ₹4L/mo', experience: '8+ Years', type: 'Full Time', badge: 'Urgent', badgeColor: 'bg-red-100 text-red-600', typeColor: 'bg-sky-50 text-sky-600 border-sky-100', initials: 'A', color: '#0369A1' },
    { title: 'ICU Nurse Specialist', hospital: 'Fortis Healthcare', location: 'Delhi, DL', salary: '₹80K – ₹1.2L/mo', experience: '3+ Years', type: 'Full Time', badge: 'Hot', badgeColor: 'bg-orange-100 text-orange-600', typeColor: 'bg-sky-50 text-sky-600 border-sky-100', initials: 'F', color: '#B91C1C' },
    { title: 'Medical Lab Scientist', hospital: 'Narayana Health', location: 'Bangalore, KA', salary: '₹55K – ₹80K/mo', experience: '2+ Years', type: 'Full Time', badge: 'New', badgeColor: 'bg-green-100 text-green-600', typeColor: 'bg-sky-50 text-sky-600 border-sky-100', initials: 'N', color: '#1D4ED8' },
    { title: 'Radiologist', hospital: 'Manipal Hospitals', location: 'Hyderabad, TS', salary: '₹1.8L – ₹3L/mo', experience: '5+ Years', type: 'Contract', badge: 'Featured', badgeColor: 'bg-indigo-100 text-indigo-600', typeColor: 'bg-teal-50 text-teal-600 border-teal-100', initials: 'M', color: '#0F766E' },
    { title: 'Physiotherapist', hospital: 'Max Healthcare', location: 'Chennai, TN', salary: '₹45K – ₹70K/mo', experience: '1+ Years', type: 'Part Time', badge: 'New', badgeColor: 'bg-green-100 text-green-600', typeColor: 'bg-purple-50 text-purple-600 border-purple-100', initials: 'M', color: '#C2410C' },
    { title: 'Clinical Pharmacist', hospital: 'Aster DM Healthcare', location: 'Kochi, KL', salary: '₹60K – ₹90K/mo', experience: '2+ Years', type: 'Full Time', badge: 'Hot', badgeColor: 'bg-orange-100 text-orange-600', typeColor: 'bg-sky-50 text-sky-600 border-sky-100', initials: 'A', color: '#7C3AED' },
];

const JobCard = ({ job, index }) => (
    <motion.article
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.5, delay: index * 0.08 }}
        className="hover-lift bg-white rounded-2xl p-6 shadow-lg shadow-slate-100/80 border border-slate-100 flex flex-col group"
        aria-label={`${job.title} at ${job.hospital}`}
    >
        {/* Top row — logo + badge + type */}
        <div className="flex items-start justify-between mb-4">
            <div className="flex items-center gap-3">
                <div
                    className="w-11 h-11 rounded-xl flex items-center justify-center text-white font-bold text-base shadow-md flex-shrink-0"
                    style={{ background: `linear-gradient(135deg, ${job.color}, ${job.color}cc)` }}
                    aria-hidden="true"
                >
                    {job.initials}
                </div>
                <div className="flex flex-col gap-0.5">
                    <div className="text-xs text-slate-400 font-medium leading-none">{job.hospital}</div>
                    <span className={`inline-block px-2 py-0.5 rounded-full text-[11px] font-bold ${job.badgeColor}`}>{job.badge}</span>
                </div>
            </div>
            <span className={`px-2.5 py-1 rounded-full text-xs font-semibold border ${job.typeColor} flex-shrink-0`}>{job.type}</span>
        </div>

        {/* Job Title */}
        <h3 className="text-base font-bold text-slate-900 mb-3 group-hover:text-sky-600 transition-colors leading-snug">{job.title}</h3>

        {/* Meta */}
        <div className="flex flex-wrap gap-3 text-xs text-slate-500 mb-4">
            <span className="flex items-center gap-1">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
                </svg>
                {job.location}
            </span>
            <span className="flex items-center gap-1">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                    <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="2" />
                    <path d="M12 6v6l4 2" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
                </svg>
                {job.experience} exp.
            </span>
        </div>

        {/* Bottom row — salary + apply */}
        <div className="flex items-center justify-between mt-auto pt-3 border-t border-slate-100">
            <div>
                <div className="text-[10px] text-slate-400 uppercase tracking-wide font-semibold">Salary</div>
                <div className="font-bold text-green-600 text-sm">{job.salary}</div>
            </div>
            <button
                className="btn-ripple px-4 py-2 bg-gradient-to-r from-sky-500 to-teal-500 text-white text-xs font-bold rounded-xl hover:shadow-lg hover:shadow-sky-200 hover:-translate-y-0.5 transition-all duration-300"
                aria-label={`Apply for ${job.title}`}
            >
                Apply Now
            </button>
        </div>
    </motion.article>
);

const FeaturedJobs = () => (
    <section className="py-24 px-4 sm:px-6 lg:px-8 bg-slate-50" aria-label="Featured jobs">
        <div className="max-w-7xl mx-auto">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                className="flex flex-col sm:flex-row items-start sm:items-end justify-between mb-12 gap-4"
            >
                <div>
                    <span className="inline-block px-4 py-1.5 rounded-full bg-sky-50 text-sky-600 text-xs font-bold uppercase tracking-widest mb-3 border border-sky-100">Top Openings</span>
                    <h2 className="text-4xl font-bold text-slate-900 leading-tight">Featured Jobs</h2>
                    <p className="text-slate-500 mt-1.5 text-sm">Handpicked from 15,000+ verified positions</p>
                </div>
                <a
                    href="#"
                    className="inline-flex items-center gap-2 px-5 py-2.5 border border-sky-200 text-sky-600 font-semibold rounded-xl hover:bg-sky-50 transition-all duration-200 text-sm flex-shrink-0"
                >
                    View All Jobs
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                        <path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                </a>
            </motion.div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {jobs.map((job, i) => <JobCard key={job.title} job={job} index={i} />)}
            </div>
        </div>
    </section>
);

export default FeaturedJobs;
