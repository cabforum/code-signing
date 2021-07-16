Version 1.2 (DATE)


Baseline Requirements
for the
Issuance and Management
of
Publicly-Trusted Code Signing Certificates 


This work is licensed under the Creative Commons Attribution 4.0 International license.


9.3	Certificate Policy Identification
This section sets forth minimum requirements for the content of the Subscriber, Subordinate CA, and Root CA Certificates, as they relate to the identification of Certificate Policy. 


11.	Verification Practices


11.2	Verification of Individual Applicants 
Prior to issuing a Code Signing Certificate to an Individual Applicant, the CA MUST:
1.	Verify the Subject’s identity under Section 11.2.1 of this document, and 
2.	Verify the authenticity of the identity under Section 11.2.2 of this document. 

11.2.1	Individual Identity
The CA MUST verify the Applicant’s identity using one of the following processes:
1.	 	The CA MUST obtain a legible copy, which discernibly shows the Requester’s face, of at least one currently valid government-issued photo ID (passport, driver’s license, military ID, national ID, or equivalent document type).  The CA MUST inspect the copy for any indication of alteration or falsification. The CA MUST also verify the address of the Requester using (i) a government-issued photo ID, (ii) a QIIS or QGIS, or (iii) an access code to activate the Certificate where the access code was physically mailed to the Requester; OR
2.	 The CA MUST have the Requester digitally sign the Certificate Request using a valid personal Certificate that was issued under one of the following adopted standards: Qualified Certificates issued pursuant to ETSI TS 101 862, IGTF, Adobe Signing Certificate issued under the AATL or CDS program, the Kantara identity assurance framework at level 2, NIST SP 800-63 at level 2, or the FBCA CP at Basic or higher assurance. 

11.2.2	Authenticity of Identity
The CA MUST verify the authenticity of the Certificate Request using one of the following:
1.	Having the Requester provide a photo of the Requester holding the submitted government-issued photo ID where the photo is of sufficient quality to read both the name listed on the photo ID and the issuing authority; OR
2.	Having the CA perform an in-person or web camera-based verification of the Requester where an employee or contractor of the CA can see the Requester, review the Requester’s photo ID, and confirm that the Requester is the individual identified in the submitted photo ID; OR
3.	Having the CA obtain an executed Declaration of Identity of the Requester that includes at least one unique biometric identifier (such as a fingerprint or handwritten signature).  The CA MUST confirm the document’s authenticity directly with the Verifying Person using contact information confirmed with a QIIS or QGIS; OR
4.	Verifying that the digital signature used to sign the Request under Section 11.2.1(2) is a valid signature and originated from a Certificate issued at the appropriate level of assurance as evidenced by the certificate chain.  Acceptable verification under this section includes validation that the Certificate was issued by a CA qualified by the entity responsible for adopting, enforcing, or maintaining the adopted standard and chains to an intermediate certificate or root certificate designated as complying with such standard. 


11.7	  Processing High Risk Applications 
CAs MUST not issue new or replacement Code Signing Certificates to an entity that the CA determined intentionally signed Suspect Code.  The CA MUST keep meta-data about the reason for revoking a Code Signing Certificate as proof that the Code Signing Certificate was not revoked because the Applicant was intentionally signing Suspect Code.
CAs MAY issue new or replacement Code Signing Certificates to an entity who is the victim of a documented Takeover Attack, resulting in either a loss of control of their code-signing service or loss of the Private Key associated with their Code Signing Certificate.  
If the CA is aware that the Applicant was the victim of a Takeover Attack, the CA MUST verify that the Applicant is protecting its Code Signing Private Keys under Section 16.3(1) or Section 16.3(2).  The CA MUST verify the Applicant’s compliance with Section 16.3(1) or Section 16.3(2) (i) through technical means that confirm the Private Keys are protected using the method described in 16.3(1) or 16.3.2(2) or (ii) by relying on a report provided by the Applicant that is signed by an auditor who is approved by the CA and who has IT and security training or is a CISA.
Documentation of a Takeover Attack MAY include a police report (validated by the CA) or public news report that admits that the attack took place.  The Subscriber MUST provide a report from an auditor with IT and security training or a CISA that provides information on how the Subscriber was storing and using Private keys and how the intended solution for better security meets the guidelines for improved security.
Except where issuance is expressly authorized by the Application Software Supplier, CAs MUST not issue new Code Signing Certificates to an entity where the CA is aware that the entity has been the victim of two Takeover Attacks or where the CA is aware that entity breached a requirement under this Section to protect Private Keys under either Section 16.3(1) or 16.3(2).

11.8	Due Diligence
1. 	The results of the verification processes and procedures outlined in these Requirements are intended to be viewed both individually and as a group. Thus, after all of the verification processes and procedures are completed, the CA MUST have a person who is not responsible for the collection of information review all of the information and  documentation assembled in support of the Code Signing Certificate application and look for discrepancies or other details requiring further explanation.
2.	The CA MUST obtain and document further explanation or clarification from Applicant and other sources of information, as necessary, to resolve those discrepancies or details that require further explanation. 
3.	The CA MUST refrain from issuing a Code Signing Certificate until all of the information and documentation assembled in support of the Certificate is such that issuance of the Certificate will not communicate factual information that the CA knows, or with the exercise of due diligence should discover from the assembled information and documentation, to be inaccurate.  If satisfactory explanation and/or additional documentation are not received within a reasonable time, the CA MUST decline the Certificate request and SHOULD notify the Applicant accordingly.

13.1.7	Certificate Revocation Date
When revoking a Certificate, the CA SHOULD work with the Subscriber to estimate a date of when the revocation should occur in order to mitigate the impact of revocation on validly signed Code.  For key compromise events, this date SHOULD be the earliest date of suspected compromise.  

14.	Employees and Third Parties


16.	Data Security and Private Key Protection
The requirements in BR Sections 6.1 and 6.2 apply equally to Code Signing Certificates.  In addition:

16.1	Timestamp Authority Key Protection 
1.	Each CA MUST operate an RFC-3161-compliant Timestamp Authority that is available for use by customers of its Code Signing Certificates.  CAs MUST recommend to Subscribers that they use the CA’s Timestamping Authority to time-stamp signed code.
2.	A Timestamp Authority MUST protect its signing key using a process that is at least to FIPS 140-2 Level 3, Common Criteria EAL 4+ (ALC_FLR.2), or higher.  The CA MUST protect its signing operations in accordance with the CA/Browser Forum’s Network Security Guidelines.  Any changes to its signing process MUST be an auditable event. 
3.	The Timestamp Authority MUST ensure that clock synchronization is maintained when a leap second occurs.  A Timestamp Authority MUST synchronize its timestamp server at least every 24 hours with a UTC(k) time source.  The timestamp server MUST automatically detect and report on clock drifts or jumps out of synchronization with UTC.  Clock adjustments of one second or greater MUST be auditable events.

16.2	Signing Service Requirements
The Signing Service MUST ensure that a Subscriber’s private key is generated, stored, and used in a secure environment that has controls to prevent theft or misuse.  A Signing Service MUST enforce multi-factor authentication to access and authorize Code Signing and obtain a representation from the Subscriber that they will securely store the tokens required for multi-factor access.  A system used to host a Signing Service MUST NOT be used for web browsing.  The Signing Service MUST run a regularly updated antivirus solution to scan the service for possible virus infection.  The Signing Service MUST comply with the Network Security Guidelines as a “Delegated Third Party”.

16.3	Subscriber Private Key Protection
The CA MUST obtain a representation from the Subscriber that the Subscriber will use one of the following options to generate and protect their Code Signing Certificate private keys: 
1.	A Trusted Platform Module (TPM) that generates and secures a key pair and that can document the Subscriber’s private key protection through a TPM key attestation.  
2.	A hardware crypto module with a unit design form factor certified as conforming to at least FIPS 140 Level 2, Common Criteria EAL 4+, or equivalent.  
3.	Another type of hardware storage token with a unit design form factor of SD Card or USB token (not necessarily certified as conformant with FIPS 140 Level 2 or Common Criteria EAL 4+). The Subscriber MUST also warrant that it will keep the token physically separate from the device that hosts the code signing function until a signing session is begun.  
A CA MUST recommend that the Subscriber protect Private Keys using the method described in Section 16.3(1) or 16.3(2) over the method described in Section 16.3(3) and obligate the Subscriber to protect Private Keys in accordance with 10.3.2(2).


18.	Liability and Indemnification
As specified in BR Section 9.
 

(5) Timestamp Certificates

A.	certificatePolicies
This extension MUST be present and SHOULD NOT be marked critical.
certificatePolicies:policyIdentifier (Required)
•	A Policy Identifier, defined by the Issuer, that indicates a Certificate Policy asserting the Issuer's adherence to and compliance with these Requirements.
certificatePolicies:policyQualifiers:policyQualifierId (Recommended)
•	id-qt 1 [RFC 5280]
certificatePolicies:policyQualifiers:qualifier:cPSuri (Optional)
•	HTTP URL for the Subordinate CA's Certification Practice Statement

B.	cRLDistributionPoint
This extension MAY be present.  If present, it MUST NOT be marked critical, and it MUST contain the HTTP URL of the CA’s CRL service.  

C.	authorityInformationAccess
This extension MUST be present and MUST NOT be marked critical.  The extension MUST contain the HTTP URL of the CA’s OCSP responder (accessMethod = 1.3.6.1.5.5.7.48.1) and the HTTP URL for the Root CA’s certificate (accessMethod = 1.3.6.1.5.5.7.48.2). 

D.	basicConstraints (optional)
If present, the cA field MUST be set false. 

E.	keyUsage (required)
This extension MUST be present and MUST be marked critical. The bit positions for digitalSignature MUST be set.  Bit positions for keyCertSign and cRLSign MUST NOT be set. All other bit positions SHOULD NOT be set.

F.	extKeyUsage (EKU) (required)
The value id-kp-timeStamping [RFC5280] MUST be present and MUST be marked critical.  
The value anyExtendedKeyUsage (2.5.29.37.0) MUST NOT be present.   
Other values SHOULD NOT be present.  If any other value is present, the CA MUST have a business agreement with a Platform vendor requiring that EKU in order to issue a Platform-specific code signing certificate with that EKU.
The CA MUST set all other fields and extensions in accordance to RFC 5280.


 
Appendix D

HIGH RISK REGIONS OF CONCERN 

The geographic locations listed below have more than 5% of the Code Signing Certificates for that location associated with signed Suspect Code when compared to the number of all Code Signing Certificates for that area.  Applications originating or associated from one of these HRRCs are considered high risk and require additional verification as specified under Section 11.7 of this document:

NONE
