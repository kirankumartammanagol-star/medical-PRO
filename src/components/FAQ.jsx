import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

const faqs = [
    {
        q: 'How does credential verification work?',
        a: 'Our AI-powered system cross-references your medical license and certifications with official databases including NMC, state medical councils, and nursing registries. Verification typically completes within 2–24 hours. Once verified, you receive a digital verification badge displayed prominently on your profile.',
    },
    {
        q: 'How does AI job matching work?',
        a: 'Our proprietary machine learning algorithm analyzes your profile, skills, experience, specialization, preferred location, and salary expectations. It then matches you with relevant job openings based on over 50 parameters, achieving a 98% candidate-job compatibility accuracy rate.',
    },
    {
        q: 'Can hospitals post jobs directly?',
        a: 'Yes! Hospitals and healthcare organizations can register as employers, post unlimited job listings, set screening criteria, and access our AI-powered applicant ranking system. Our enterprise dashboard provides full pipeline visibility, analytics, and compliance tracking.',
    },
    {
        q: 'Is my personal and professional data secure?',
        a: 'Absolutely. We are fully HIPAA compliant and use AES-256 encryption for all data at rest and TLS 1.3 for data in transit. Your information is never sold to third parties. You have full control over your profile visibility and can delete your data at any time.',
    },
    {
        q: 'What specializations and roles are supported?',
        a: 'HealthCareer Pro supports 200+ healthcare specializations including physicians (all branches), nurses, allied health professionals, lab scientists, radiologists, physiotherapists, pharmacists, healthcare administrators, and more. Our network spans hospitals, clinics, diagnostics, and pharmaceutical companies.',
    },
];

const FAQItem = ({ faq, index }) => {
    const [open, setOpen] = useState(false);

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: index * 0.08 }}
            className="border border-slate-200 rounded-2xl overflow-hidden hover:border-sky-200 transition-colors duration-200"
        >
            <button
                className={`w-full flex items-center justify-between p-6 text-left transition-colors duration-200 ${open ? 'bg-sky-50' : 'bg-white hover:bg-slate-50'}`}
                onClick={() => setOpen(!open)}
                aria-expanded={open}
                aria-controls={`faq-answer-${index}`}
            >
                <span className="font-semibold text-slate-900 pr-4 text-sm sm:text-base">{faq.q}</span>
                <motion.div
                    animate={{ rotate: open ? 45 : 0 }}
                    transition={{ duration: 0.2 }}
                    className="flex-shrink-0 w-8 h-8 rounded-full bg-gradient-to-br from-sky-500 to-teal-400 flex items-center justify-center"
                    aria-hidden="true"
                >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                        <path d="M12 5v14M5 12h14" stroke="white" strokeWidth="2.5" strokeLinecap="round" />
                    </svg>
                </motion.div>
            </button>

            <AnimatePresence initial={false}>
                {open && (
                    <motion.div
                        id={`faq-answer-${index}`}
                        key="answer"
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: 'auto', opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.3, ease: 'easeInOut' }}
                        className="overflow-hidden"
                    >
                        <div className="px-6 pb-6 pt-2 text-slate-500 text-sm leading-relaxed bg-sky-50 border-t border-sky-100">
                            {faq.a}
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </motion.div>
    );
};

const FAQ = () => (
    <section className="py-24 px-4 sm:px-6 lg:px-8 bg-white" aria-label="Frequently asked questions">
        <div className="max-w-3xl mx-auto">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                className="text-center mb-14"
            >
                <span className="inline-block px-4 py-1.5 rounded-full bg-sky-50 text-sky-600 text-xs font-bold uppercase tracking-widest mb-4 border border-sky-100">FAQ</span>
                <h2 className="text-4xl font-bold text-slate-900 mb-4">Frequently Asked Questions</h2>
                <p className="text-slate-500">Got questions? We have answers. Can't find what you're looking for? <a href="#contact" className="text-sky-500 font-semibold hover:underline">Contact us</a>.</p>
            </motion.div>

            <div className="space-y-4">
                {faqs.map((faq, i) => <FAQItem key={i} faq={faq} index={i} />)}
            </div>
        </div>
    </section>
);

export default FAQ;
