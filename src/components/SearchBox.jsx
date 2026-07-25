import React, { useState } from 'react';


const popularTags = ['Doctor', 'Nurse', 'Lab Technician', 'Radiologist', 'Physiotherapist', 'Pharmacist'];

const SearchBox = () => {
    const [activeTag, setActiveTag] = useState(null);

    return (
        <section id="jobs" className="py-16 px-4 sm:px-6 lg:px-8" aria-label="Job search">
            <div className="max-w-5xl mx-auto">
                <div
                    className="bg-white rounded-3xl p-8 shadow-2xl shadow-sky-100/50 border border-slate-100"
                    style={{ outline: '1.5px solid transparent', backgroundImage: 'linear-gradient(white,white), linear-gradient(135deg,#0EA5E9,#14B8A6,#6366F1)', backgroundOrigin: 'border-box', backgroundClip: 'padding-box, border-box' }}
                >
                    {/* Header */}
                    <div className="mb-6">
                        <h2 className="text-2xl font-bold text-slate-900 leading-tight">Find Healthcare Jobs</h2>
                        <p className="text-slate-500 text-sm mt-1">Search from 15,000+ verified healthcare positions</p>
                    </div>

                    {/* Fields */}
                    <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-5">

                        {/* Job Title */}
                        <div className="flex flex-col gap-1.5">
                            <label className="text-xs font-semibold text-slate-500 uppercase tracking-wide" htmlFor="job-title">Job Title</label>
                            <div className="relative">
                                <svg className="absolute left-3 top-1/2 -translate-y-1/2 text-sky-400 pointer-events-none" width="17" height="17" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                    <rect x="2" y="7" width="20" height="14" rx="2" stroke="currentColor" strokeWidth="2" />
                                    <path d="M16 7V5c0-1.105-.895-2-2-2h-4C8.895 3 8 3.895 8 5v2" stroke="currentColor" strokeWidth="2" />
                                </svg>
                                <input
                                    id="job-title"
                                    type="text"
                                    placeholder="e.g. Senior Cardiologist"
                                    className="w-full h-11 pl-10 pr-4 rounded-xl border border-slate-200 focus:border-sky-400 focus:ring-2 focus:ring-sky-100 outline-none text-sm text-slate-700 bg-slate-50 focus:bg-white transition-all duration-200"
                                />
                            </div>
                        </div>

                        {/* Location */}
                        <div className="flex flex-col gap-1.5">
                            <label className="text-xs font-semibold text-slate-500 uppercase tracking-wide" htmlFor="location">Location</label>
                            <div className="relative">
                                <svg className="absolute left-3 top-1/2 -translate-y-1/2 text-sky-400 pointer-events-none" width="17" height="17" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                    <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" fill="currentColor" />
                                </svg>
                                <input
                                    id="location"
                                    type="text"
                                    placeholder="e.g. Mumbai, Delhi"
                                    className="w-full h-11 pl-10 pr-4 rounded-xl border border-slate-200 focus:border-sky-400 focus:ring-2 focus:ring-sky-100 outline-none text-sm text-slate-700 bg-slate-50 focus:bg-white transition-all duration-200"
                                />
                            </div>
                        </div>

                        {/* Specialization */}
                        <div className="flex flex-col gap-1.5">
                            <label className="text-xs font-semibold text-slate-500 uppercase tracking-wide" htmlFor="specialization">Specialization</label>
                            <div className="relative">
                                <svg className="absolute left-3 top-1/2 -translate-y-1/2 text-sky-400 pointer-events-none" width="17" height="17" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                    <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="2" />
                                    <path d="M12 8v4M12 16h.01" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
                                </svg>
                                <select
                                    id="specialization"
                                    className="w-full h-11 pl-10 pr-4 rounded-xl border border-slate-200 focus:border-sky-400 focus:ring-2 focus:ring-sky-100 outline-none text-sm text-slate-700 bg-slate-50 focus:bg-white transition-all duration-200 appearance-none cursor-pointer"
                                >
                                    <option value="">All Specializations</option>
                                    <option>Cardiology</option>
                                    <option>Neurology</option>
                                    <option>Orthopedics</option>
                                    <option>Pediatrics</option>
                                    <option>Oncology</option>
                                    <option>Emergency Medicine</option>
                                    <option>Radiology</option>
                                    <option>Anesthesiology</option>
                                </select>
                                <svg className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none" width="14" height="14" viewBox="0 0 24 24" fill="none">
                                    <path d="M6 9l6 6 6-6" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                                </svg>
                            </div>
                        </div>
                    </div>

                    {/* Search Button */}
                    <button
                        className="btn-ripple w-full h-12 bg-gradient-to-r from-sky-500 to-teal-500 text-white font-bold rounded-2xl hover:shadow-xl hover:shadow-sky-200 hover:-translate-y-0.5 transition-all duration-300 flex items-center justify-center gap-2 text-sm"
                        aria-label="Search healthcare jobs"
                    >
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                            <circle cx="11" cy="11" r="8" stroke="white" strokeWidth="2.5" />
                            <path d="M21 21l-4.35-4.35" stroke="white" strokeWidth="2.5" strokeLinecap="round" />
                        </svg>
                        Search Jobs
                    </button>

                    {/* Popular Tags */}
                    <div className="mt-5 flex flex-wrap items-center gap-2">
                        <span className="text-xs font-semibold text-slate-400">Popular:</span>
                        {popularTags.map((tag) => (
                            <button
                                key={tag}
                                onClick={() => setActiveTag(activeTag === tag ? null : tag)}
                                className={`px-3 py-1.5 rounded-full text-xs font-semibold border transition-all duration-200 hover:-translate-y-0.5 ${activeTag === tag
                                        ? 'bg-sky-500 text-white border-sky-500 shadow-md shadow-sky-200'
                                        : 'bg-white text-slate-600 border-slate-200 hover:border-sky-300 hover:text-sky-600'
                                    }`}
                                aria-pressed={activeTag === tag}
                            >
                                {tag}
                            </button>
                        ))}
                    </div>
                </div>
            </div>
        </section>
    );
};

export default SearchBox;
