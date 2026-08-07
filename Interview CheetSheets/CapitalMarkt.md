# SWIFT / Financial Messaging (Interview Notes)

## What is SWIFT?
SWIFT (Society for Worldwide Interbank Financial Telecommunication) is a global messaging network used by banks and financial institutions to exchange secure and standardized financial messages.

> **Important:** SWIFT only sends messages. It does **not** transfer money or securities. :contentReference[oaicite:0]{index=0}

---

# ISO 15022

## What is it?
ISO 15022 is the older SWIFT messaging standard.

- Uses MT (Message Type) messages.
- Widely used in securities and payments.
- Messages are fixed-format and field-based.

## Examples
- MT103
- MT202
- MT540
- MT548

## Interview Answer
> ISO 15022 is the traditional SWIFT messaging standard that uses MT messages for payments and securities processing.

---

# ISO 20022

## What is it?
ISO 20022 is the newer financial messaging standard.

- XML-based
- More structured
- Supports richer business data
- Replacing many ISO 15022 messages

## Example
- sese.030

## Interview Answer
> ISO 20022 is the next-generation financial messaging standard that provides richer and more structured data than ISO 15022.

---

# SWIFT Message Exchange

## What is it?
It is the process of exchanging financial messages between institutions.

Typical Flow:

Bank A
↓
SWIFT Network
↓
Bank B

Messages exchanged include:
- Payment messages
- Settlement messages
- Confirmation messages
- Status updates

## Interview Answer
> SWIFT Message Exchange is the secure communication process through which banks exchange standardized financial messages.

---

# Settlement Messages

## What are they?
Settlement messages are used during securities settlement.

They instruct:
- Buy securities
- Sell securities
- Receive securities
- Deliver securities
- Settlement status

Most common:
- MT540–MT548

---

# Corporate Action Processing

## What is it?

Corporate actions are events initiated by a company that affect investors.

Examples:
- Dividend
- Bonus Issue
- Stock Split
- Rights Issue
- Merger

Banks exchange SWIFT messages to notify and process these events.

## Interview Answer
> Corporate Action Processing is the handling of events like dividends, stock splits, and mergers using standardized SWIFT messages.

---

# MT530

## Purpose
Settlement Instruction Request

## Used For
Request settlement instructions before settlement.

## Simple Example
A custodian requests settlement details before processing a trade.

## Interview Answer
> MT530 is used to request settlement instructions for a securities transaction.

---

# MT540

## Purpose
Receive Free

## Meaning
Receive securities without payment.

## Example
Free transfer of shares between accounts.

## Money Movement?
❌ No

## Interview Answer
> MT540 is used to receive securities without any cash payment.

---

# MT541

## Purpose
Receive Against Payment (RAP)

## Meaning
Receive securities after making payment.

## Example
Buying shares from another institution.

## Money Movement?
✅ Yes

## Interview Answer
> MT541 is used when securities are received only after payment is made.

---

# MT542

## Purpose
Deliver Free

## Meaning
Deliver securities without payment.

## Example
Gift transfer or internal transfer.

## Money Movement?
❌ No

## Interview Answer
> MT542 delivers securities without exchanging cash.

---

# MT543

## Purpose
Deliver Against Payment (DAP)

## Meaning
Deliver securities after receiving payment.

## Example
Selling securities.

## Money Movement?
✅ Yes

## Interview Answer
> MT543 delivers securities only after payment is received.

---

# MT544

## Purpose
Receive Free Confirmation

## Meaning
Confirms free receipt of securities.

## Interview Answer
> MT544 confirms that securities were successfully received without payment.

---

# MT545

## Purpose
Receive Against Payment Confirmation

## Meaning
Confirms receipt after payment.

## Interview Answer
> MT545 confirms successful receipt of securities against payment.

---

# MT546

## Purpose
Deliver Free Confirmation

## Meaning
Confirms free delivery of securities.

## Interview Answer
> MT546 confirms successful delivery of securities without payment.

---

# MT547

## Purpose
Deliver Against Payment Confirmation

## Meaning
Confirms delivery after payment.

## Interview Answer
> MT547 confirms successful delivery of securities against payment.

---

# MT548

## Purpose
Settlement Status and Processing Advice

## Meaning
Provides settlement status.

## Common Status
- Pending
- Matched
- Settled
- Failed
- Cancelled

## Interview Answer
> MT548 provides the current status of a settlement instruction.

---

# MT596

## Purpose
Statement of Fees

## Meaning
Communicates settlement-related charges and fees.

## Example
Custody fees
Settlement fees

## Interview Answer
> MT596 communicates charges or fees associated with settlement processing.

---

# MT598

## Purpose
Free Format Message

## Meaning
Used for manual communication between institutions.

## Example
Additional settlement instructions
Operational queries
Clarifications

## Interview Answer
> MT598 is a free-format SWIFT message used for operational communication.

---

# MT103

## Purpose
Single Customer Credit Transfer

## Meaning
Transfers money from one customer to another.

## Example
Customer sends ₹1,00,000 internationally.

## Used In
Payments

## Interview Answer
> MT103 is used for international customer-to-customer fund transfers.

---

# MT202

## Purpose
Bank-to-Bank Transfer

## Meaning
Transfers funds between financial institutions.

## Example
Settlement between correspondent banks.

## Used In
Interbank payments

## Interview Answer
> MT202 is used for transferring funds between banks.

---

# ISO 20022 - sese.030

## Purpose
Securities Settlement Transaction Status Advice

## Replaces
MT548 (in many implementations)

## Used For
- Pending
- Matched
- Settled
- Failed
- Cancelled

## Interview Answer
> sese.030 is the ISO 20022 message used to communicate securities settlement status.

---

# Quick MT540–MT548 Summary

| Message | Meaning | Payment? |
|----------|---------|----------|
| MT540 | Receive Free | ❌ |
| MT541 | Receive Against Payment | ✅ |
| MT542 | Deliver Free | ❌ |
| MT543 | Deliver Against Payment | ✅ |
| MT544 | Confirmation - Receive Free | ❌ |
| MT545 | Confirmation - Receive Against Payment | ✅ |
| MT546 | Confirmation - Deliver Free | ❌ |
| MT547 | Confirmation - Deliver Against Payment | ✅ |
| MT548 | Settlement Status | Depends |

---

# ISO 15022 vs ISO 20022

| ISO 15022 | ISO 20022 |
|------------|------------|
| MT Messages | XML Messages |
| Older Standard | New Standard |
| Less Data | Rich Data |
| Field Based | Structured XML |
| Widely Used | Future Standard |

---

# Payment vs Securities Messages

## Payment Messages
- MT103
- MT202

Used for transferring money.

---

## Securities Messages
- MT530
- MT540
- MT541
- MT542
- MT543
- MT544
- MT545
- MT546
- MT547
- MT548
- sese.030

Used for securities settlement.

---

# Asset Management

## What is it?
Managing investments like stocks, bonds, and mutual funds on behalf of clients to grow their money.

## Easy Example
A mutual fund company invests your money in different stocks and bonds.

## Interview Answer
> Asset Management is the process of managing client investments to maximize returns while controlling risk.

---

# Investment Operations

## What is it?
The back-office process that supports investment activities after a trade is placed.

## Includes
- Trade processing
- Settlement
- Reconciliation
- Reporting

## Easy Example
After a trader buys a bond, the operations team ensures it settles correctly.

## Interview Answer
> Investment Operations handles all post-trade activities to ensure transactions are processed accurately.

---

# Capital Markets

## What is it?
A financial market where long-term securities like stocks and bonds are bought and sold.

## Easy Example
A company issues bonds to raise money from investors.

## Interview Answer
> Capital Markets allow companies and governments to raise funds by issuing securities.

---

# Trade Lifecycle

## What is it?
The complete journey of a trade from execution to settlement.

## Steps
1. Trade Execution
2. Trade Confirmation
3. Settlement
4. Reconciliation

## Easy Example
You buy a bond → trade is confirmed → payment is made → securities are delivered.

## Interview Answer
> Trade Lifecycle is the end-to-end process of a trade from execution until settlement.

---

# Trade Confirmation

## What is it?
Verification that buyer and seller agree on trade details.

## Easy Example
Both parties confirm price, quantity, and settlement date.

## Interview Answer
> Trade Confirmation ensures both parties agree on all trade details before settlement.

---

# Trade Settlement

## What is it?
The actual exchange of securities and money.

## Easy Example
Buyer pays cash and receives bonds.

## Interview Answer
> Trade Settlement is the process where cash and securities are exchanged.

---

# Reconciliation

## What is it?
Comparing records between two systems to ensure they match.

## Easy Example
Bank records are compared with custodian records.

## Interview Answer
> Reconciliation verifies that all trade records match across different systems.

---

# Custody Services

## What is it?
Safe keeping of securities on behalf of investors.

## Services
- Hold securities
- Collect dividends
- Process corporate actions

## Easy Example
A bank safely stores your shares electronically.

## Interview Answer
> Custody Services securely hold client securities and process related activities.

---

# Settlement Processing

## What is it?
Processing all activities required to complete settlement.

## Includes
- Validate trade
- Check cash
- Check securities
- Send SWIFT messages

## Interview Answer
> Settlement Processing ensures securities and cash are exchanged successfully.

---

# US Fixed Income

## What is it?
Debt securities issued in the US market.

## Examples
- Treasury Bonds
- Corporate Bonds
- Municipal Bonds

## Interview Answer
> US Fixed Income refers to debt securities that provide regular interest payments.

---

# T2S Settlement

## What is it?
Target2-Securities (Europe's common settlement platform).

## Benefit
One platform for settling securities across Europe.

## Interview Answer
> T2S is a European platform that standardizes securities settlement across participating countries.

---

# Non-T2S Settlement

## What is it?
Settlement performed outside the T2S platform.

## Example
Local market settlement systems.

## Interview Answer
> Non-T2S Settlement refers to settlements processed outside the European T2S platform.

---

# Corporate Bonds

## What is it?
Bonds issued by companies to raise money.

## Easy Example
A company borrows ₹100 crore from investors and pays interest.

## Interview Answer
> Corporate Bonds are debt securities issued by companies to raise capital.

---

# Asset-Backed Securities (ABS)

## What is it?
Securities backed by a pool of assets.

## Assets Can Be
- Home loans
- Car loans
- Credit card loans

## Easy Example
Many car loans are combined and sold as one investment.

## Interview Answer
> Asset-Backed Securities are investments backed by a collection of loans or receivables.

---

# Trust Structures

## What is it?
A legal structure where assets are managed by a trustee for investors.

## Easy Example
A trustee manages loan payments and distributes money to investors.

## Interview Answer
> Trust Structures hold and manage assets on behalf of investors through a trustee.