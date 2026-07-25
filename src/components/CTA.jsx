import React from 'react';
import { motion } from 'framer-motion';

const CTA = () => (
    <section className="py-24 px-4 sm:px-6 lg:px-8 relative overflow-hidden" aria-label="Call to action">
        {/* Gradient background */}
        <div className="absolute inset-0 bg-gradient-to-br from-sky-600 via-sky-500 to-teal-500" aria-hidden="true" />
        {/* Pattern overlay */}
        <div className="absolute inset-0 opacity-10" aria-hidden="true">
            <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                        <path d="M 40 0 L 0 0 0 40" fill="none" stroke="white" strokeWidth="1" />
                    </pattern>
                </defs>
                <rect width="100%" height="100%" fill="url(#grid)" />
            </svg>
        </div>

        {/* Blobs */}
        <div className="absolute -top-20 -right-20 w-80 h-80 bg-white/10 rounded-full blur-3xl" aria-hidden="true" />
        <div className="absolute -bottom-20 -left-20 w-80 h-80 bg-teal-400/30 rounded-full blur-3xl" aria-hidden="true" />

        <div className="max-w-5xl mx-auto text-center relative z-10">
            <motion.div
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.7 }}
            >
                {/* Badge */}
                <div className="inline-flex items-center gap-2 bg-white/20 border border-white/30 rounded-full px-4 py-1.5 text-sm text-white font-medium mb-6 backdrop-blur-sm">
                    <span className="w-2 h-2 bg-green-300 rounded-full animate-pulse" aria-hidden="true"></span>
                    Join 50,000+ Healthcare Professionals
                </div>

                <h2 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-white mb-6 leading-tight">
                    Ready to Transform Your<br />
                    <span className="text-teal-200">Healthcare Career?</span>
                </h2>

                <p className="text-sky-100 text-xl mb-10 max-w-2xl mx-auto leading-relaxed">
                    Join India's #1 healthcare recruitment platform. AI matching, instant credential verification, and 15,000+ active openings.
                </p>

                <div className="flex flex-wrap justify-center gap-4">
                    <a
                        href="#"
                        className="btn-ripple px-10 py-4 bg-white text-sky-600 font-bold rounded-2xl hover:bg-sky-50 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 text-lg"
                        aria-label="Get started with HealthCareer Pro"
                    >
                        Get Started Free
                    </a>
                    <a
                        href="#employers"
                        className="btn-ripple px-10 py-4 bg-white/15 border border-white/40 text-white font-bold rounded-2xl hover:bg-white/25 hover:-translate-y-1 transition-all duration-300 text-lg backdrop-blur-sm"
                        aria-label="Post jobs as a hospital or employer"
                    >
                        Post Jobs
                    </a>
                </div>

                {/* Trust indicators */}
                <div className="flex flex-wrap justify-center gap-8 mt-14">
                    {[
                        { icon: '🔒', label: 'HIPAA Compliant' },
                        { icon: '⚡', label: 'Instant Verification' },
                        { icon: '🤖', label: 'AI Powered' },
                        { icon: '🆓', label: 'Free to Join' },
                    ].map((item) => (
                        <div key={item.label} className="flex items-center gap-2 text-white/90 text-sm font-medium">
                            <span className="text-lg" aria-hidden="true">{item.icon}</span>
                            {item.label}
                        </div>
                    ))}
                </div>
            </motion.div>
        </div>
    </section>
);

export default CTA;
