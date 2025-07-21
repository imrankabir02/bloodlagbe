That's a smart decision. **Removing the login system** will make it **faster and easier** for people to register as donors and for admins to access the data in emergencies.

Here’s how you can plan this **without login/registration**, focusing on **speed and simplicity**.

---

# ✅ **Emergency Blood Donor Collection Without Login (Plan)**

## 🔴 **Objectives**

* **Collect donor information quickly.**
* **Allow hospital/admin to search and contact easily.**
* **No login, no password, no delay.**

---

## **1️⃣ System Overview**

| Page                 | Purpose                                           |
| -------------------- | ------------------------------------------------- |
| **Donor Form**       | Simple form to submit donor details               |
| **Admin View**       | Search, filter, and contact donors                |
| **Edit/Update Form** | (Optional) A link to update info with secret code |
| **Emergency Filter** | One-click search by blood group + area            |

---

## **2️⃣ Donor Form (Public, No Login)**

### Fields:

| Field              | Type            |
| ------------------ | --------------- |
| Full Name          | Text            |
| Phone Number       | Phone Field     |
| Blood Group        | Dropdown        |
| Area               | Dropdown / Text |
| Availability       | Yes / No        |
| Last Donation Date | Date (optional) |

➡ **\[ Submit Button ]**

> After submission:
> ✅ Show: "Thank you! You’re added to the life-saving donor list."

---

## **3️⃣ Admin / Hospital View (No Login, Protected Link)**

A **single protected URL** (you can hide it, password-protect it on server) for viewing the list.

### Features:

* Search by Blood Group
* Search by Area
* Filter Available Now
* Click-to-Call / SMS Buttons

Example:

```
| Name  | Blood  | Area   | Phone  | Call Now |
|-------|--------|--------|--------|----------|
| Imran | A+     | Dhaka  | 018XX  | ☎        |
```

---

## **4️⃣ Update Donor Info (Optional)**

* On submission, generate a **random 6-digit code**.
* Provide a **link like: /update/123456/**.
* Donor can later update availability or phone.

---

## **5️⃣ Technology (Simple & Fast)**

| Stack    | Recommendation                                      |
| -------- | --------------------------------------------------- |
| Backend  | Django                                              |
| Frontend | Django Template (HTML/CSS)                          |
| Database | PostgreSQL / SQLite (small scale)                   |
| Security | Protect Admin URL manually (or via basic HTTP auth) |
| SMS      | Bangladeshi SMS API (SSL Wireless, etc.)            |

---

## **6️⃣ Flow Diagram**

```
Donor ➔ Fill Form ➔ Saved in DB
Admin ➔ Access URL ➔ Search & Call
```

---

## **7️⃣ Deployment Plan**

| Time   | Task                                           |
| ------ | ---------------------------------------------- |
| Day 1  | Create simple Django app & model               |
| Day 2  | Build form & submission                        |
| Day 3  | Admin donor list with search                   |
| Day 4  | Deploy to server (DigitalOcean, AWS Free Tier) |
| Day 5  | Start collecting data                          |
| Week 2 | Inform hospitals, NGOs                         |

---

## **8️⃣ Simple UI Sketch**

### **Donor Form:**

```
[ Name     : __________ ]
[ Phone    : __________ ]
[ BloodGrp : A+ / B- ...]
[ Area     : Dhaka / ... ]
[ Available: Yes / No   ]
[ Last Donated: Date    ]
[ SUBMIT ]
```

---

### **Admin List:**

```
Filter: [ A+ ] [ Mirpur ] [ Available Now ]

| Name   | Blood | Area  | Phone    | Call  |
|--------|-------|-------|---------|-------|
| Imran  | A+    | Mirpur| 018XXXX | ☎    |
| Raju   | B-    | Banani| 017XXXX | ☎    |
```

---

## **9️⃣ Fast Action Steps for You**

1. Django `Donor` model.
2. Public `CreateView`.
3. Admin-only ListView with search.
4. Deploy.
5. Share link.

---

## **10️⃣ Suggested Domain Name**

* **bloodhelpbd.com**
* **quickbloodbd.com**
* **helpblood.org.bd**

---

If you want, I can:

* **Provide the Django models.**
* **Provide template designs (HTML).**
* **Give you ready-to-use search and filter examples.**

Let me know how you'd prefer to proceed next:
👉 **Code?**
👉 **UI Design?**
👉 **Deployment Guide?**
