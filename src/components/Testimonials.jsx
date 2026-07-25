import React from 'react';
import { motion } from 'framer-motion';

const testimonials = [
    {
        name: 'Dr. Priya Sharma',
        role: 'Senior Cardiologist',
        hospital: 'Apollo Hospitals, Mumbai',
        image: 'PS',
        color: '#0EA5E9',
        rating: 5,
        text: 'HealthCareer Pro transformed my job search. The AI matched me with my dream position at Apollo within 2 weeks. The credential verification was seamless and saved so much time. Highly recommended for any healthcare professional!',
    },
    {
        name: 'Nurse Aisha Khan',
        role: 'ICU Senior Nurse',
        hospital: 'Fortis Healthcare, Delhi',
        image: 'AK',
        color: '#14B8A6',
        rating: 5,
        text: 'The platform is incredibly user-friendly. The AI matching was spot-on — every job it recommended was relevant to my specialization. Got hired within 3 weeks. The salary analytics helped me negotiate better too!',
    },
    {
        name: 'Dr. Rajesh Menon',
        role: 'HR Director',
        hospital: 'Narayana Health, Bangalore',
        image: 'RM',
        color: '#6366F1',
        rating: 5,
        text: 'As a hospital recruiter, HealthCareer Pro has cut our hiring time by 40%. The AI screening is phenomenal — it shortlists only verified, qualified candidates. The dashboard analytics give us real visibility into our pipeline.',
    },
];

const Testimonials = () => (
    <section className="py-24 px-4 sm:px-6 lg:px-8 bg-gradient-to-br from-slate-50 to-sky-50 relative overflow-hidden" aria-label="Customer testimonials">
        <div className="absolute top-0 left-0 w-72 h-72 bg-sky-100 rounded-full blur-3xl opacity-50" aria-hidden="true" />
        <div className="absolute bottom-0 right-0 w-72 h-72 bg-indigo-100 rounded-full blur-3xl opacity-50" aria-hidden="true" />

        <div className="max-w-7xl mx-auto relative z-10">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                className="text-center mb-16"
            >
                <span className="inline-block px-4 py-1.5 rounded-full bg-sky-50 text-sky-600 text-xs font-bold uppercase tracking-widest mb-4 border border-sky-100">Testimonials</span>
                <h2 className="text-4xl sm:text-5xl font-bold text-slate-900 mb-4">What Our Community Says</h2>
                <p className="text-slate-500 max-w-xl mx-auto">Join thousands of healthcare professionals who found their dream careers</p>
            </motion.div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                {testimonials.map((t, i) => (
                    <motion.div
                        key={t.name}
                        initial={{ opacity: 0, y: 30 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ duration: 0.6, delay: i * 0.15 }}
                        className="hover-lift bg-white rounded-3xl p-8 shadow-xl shadow-slate-100/80 border border-slate-100 relative"
                    >
                        {/* Quote mark */}
                        <div className="absolute top-6 right-6 text-6xl font-serif text-sky-100 leading-none" aria-hidden="true">"</div>

                        {/* Stars */}
                        <div className="flex gap-1 mb-5" aria-label={`${t.rating} out of 5 stars`}>
                            {[...Array(t.rating)].map((_, si) => (
                                <svg key={si} width="18" height="18" viewBox="0 0 24 24" fill="#F59E0B" aria-hidden="true">
                                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                                </svg>
                            ))}
                        </div>

                        {/* Text */}
                        <p className="text-slate-600 leading-relaxed mb-6 text-sm">"{t.text}"</p>

                        {/* Author */}
                        <div className="flex items-center gap-3 border-t border-slate-100 pt-5">
                            <div
                                className="w-12 h-12 rounded-2xl flex items-center justify-center text-white font-bold text-sm shadow-md flex-shrink-0"
                                style={{ background: `linear-gradient(135deg, ${t.color}, ${t.color}99)` }}
                                aria-label={`${t.name} profile`}
                            >
                                {t.image}
                            </div>
                            <div>
                                <div className="font-bold text-slate-900 text-sm">{t.name}</div>
                                <div className="text-xs text-slate-400">{t.role}</div>
                                <div className="text-xs font-semibold mt-0.5" style={{ color: t.color }}>{t.hospital}</div>
                            </div>
                        </div>
                    </motion.div>
                ))}
            </div>
        </div>
    </section>
);

export default Testimonials;
