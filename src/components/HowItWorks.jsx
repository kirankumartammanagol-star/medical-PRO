import React from 'react';
import { motion } from 'framer-motion';

const steps = [
    {
        number: '01',
        title: 'Create Profile',
        desc: 'Build your professional healthcare profile with skills, experience, and specialty areas.',
        gradient: 'from-sky-500 to-cyan-400',
        icon: (<svg width="30" height="30" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="7" r="4" stroke="white" strokeWidth="2.5" /><path d="M5 21C5 17.134 8.134 14 12 14C15.866 14 19 17.134 19 21" stroke="white" strokeWidth="2.5" strokeLinecap="round" /></svg>),
    },
    {
        number: '02',
        title: 'Upload Certificates',
        desc: 'Submit your medical degree, licenses, NMC registration, and specialty certifications.',
        gradient: 'from-indigo-500 to-purple-500',
        icon: (<svg width="30" height="30" viewBox="0 0 24 24" fill="none"><path d="M14 2H6C5.46957 2 4.96086 2.21071 4.58579 2.58579C4.21071 2.96086 4 3.46957 4 4V20C4 20.5304 4.21071 21.0391 4.58579 21.4142C4.96086 21.7893 5.46957 22 6 22H18C18.5304 22 19.0391 21.7893 19.4142 21.4142C19.7893 21.0391 20 20.5304 20 20V8L14 2Z" stroke="white" strokeWidth="2" /><path d="M14 2V8H20M12 12V18M9 15H15" stroke="white" strokeWidth="2" strokeLinecap="round" /></svg>),
    },
    {
        number: '03',
        title: 'AI Verification',
        desc: 'Our AI verifies your credentials instantly against official medical databases and registries.',
        gradient: 'from-teal-500 to-emerald-400',
        icon: (<svg width="30" height="30" viewBox="0 0 24 24" fill="none"><path d="M12 2L4 5V11C4 15.4 7.4 19.5 12 20.5C16.6 19.5 20 15.4 20 11V5L12 2Z" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" /><path d="M9 12L11 14L15 10" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" /></svg>),
    },
    {
        number: '04',
        title: 'Get Hired',
        desc: 'Match with top hospitals, schedule interviews, and land your dream healthcare position.',
        gradient: 'from-orange-500 to-amber-400',
        icon: (<svg width="30" height="30" viewBox="0 0 24 24" fill="none"><path d="M20 7L12 3L4 7V17L12 21L20 17V7Z" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" /><path d="M12 3V21" stroke="white" strokeWidth="2" strokeLinecap="round" /><path d="M4 7L12 12L20 7" stroke="white" strokeWidth="2" strokeLinecap="round" /></svg>),
    },
];

const HowItWorks = () => (
    <section className="py-24 px-4 sm:px-6 lg:px-8 bg-slate-50 relative overflow-hidden" aria-label="How it works">
        <div className="absolute top-0 right-0 w-80 h-80 bg-gradient-to-br from-sky-100 to-teal-100 rounded-full blur-3xl opacity-60" aria-hidden="true" />
        <div className="absolute bottom-0 left-0 w-64 h-64 bg-gradient-to-br from-indigo-100 to-purple-100 rounded-full blur-3xl opacity-60" aria-hidden="true" />

        <div className="max-w-7xl mx-auto relative z-10">
            {/* Header */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                className="text-center mb-16 max-w-xl mx-auto"
            >
                <span className="inline-block px-4 py-1.5 rounded-full bg-sky-50 text-sky-600 text-xs font-bold uppercase tracking-widest mb-4 border border-sky-100">Simple Process</span>
                <h2 className="text-4xl sm:text-5xl font-bold text-slate-900 mb-4">How It Works</h2>
                <p className="text-slate-500 text-base leading-relaxed">Get started in minutes. Our streamlined process gets you from profile to hired.</p>
            </motion.div>

            {/* Steps */}
            <div className="relative">
                {/* Connecting line — desktop only */}
                <div className="hidden lg:block absolute top-[2.6rem] left-[16.66%] right-[16.66%] h-px z-0" aria-hidden="true">
                    <div className="h-full bg-gradient-to-r from-sky-300 via-indigo-300 via-teal-300 to-orange-300 opacity-60" />
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-6">
                    {steps.map((step, i) => (
                        <motion.div
                            key={step.number}
                            initial={{ opacity: 0, y: 30 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            transition={{ duration: 0.6, delay: i * 0.15 }}
                            className="flex flex-col items-center text-center"
                        >
                            {/* Icon */}
                            <div className="relative mb-6 z-10">
                                <div className={`w-[5.5rem] h-[5.5rem] rounded-3xl bg-gradient-to-br ${step.gradient} flex items-center justify-center shadow-xl`}>
                                    {step.icon}
                                </div>
                                <div className="absolute -top-2 -right-2 w-7 h-7 rounded-full bg-white border-2 border-slate-100 flex items-center justify-center shadow-md">
                                    <span className="text-[10px] font-extrabold text-slate-500">{step.number}</span>
                                </div>
                            </div>

                            <h3 className="text-lg font-bold text-slate-900 mb-2">{step.title}</h3>
                            <p className="text-slate-500 text-sm leading-relaxed max-w-[220px]">{step.desc}</p>
                        </motion.div>
                    ))}
                </div>
            </div>

            {/* CTA */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                className="flex justify-center mt-14"
            >
                <a
                    href="#"
                    className="btn-ripple inline-flex items-center gap-2 px-8 py-4 text-white font-bold rounded-2xl bg-gradient-to-r from-sky-500 to-teal-500 hover:shadow-xl hover:shadow-sky-200 hover:-translate-y-1 transition-all duration-300"
                >
                    Create Your Free Profile
                    <svg width="17" height="17" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                        <path d="M5 12h14M12 5l7 7-7 7" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                </a>
            </motion.div>
        </div>
    </section>
);

export default HowItWorks;
