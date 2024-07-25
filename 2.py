{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5e7aba04-9c30-422d-ac0f-0dd63f5248a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "An Array: [54 45 57 67 78 89]\n",
      "\n",
      "Sum: 390\n",
      "Product -1569300\n",
      "Mean: 65.0\n",
      "Standard Deviation: 14.910846164230028\n",
      "Variance 222.33333333333334\n",
      "Minimum Value: 45\n",
      "Max: 89\n",
      "Min Index: 1\n",
      "Max Index: 5\n",
      "Median: 62.0\n",
      "Product: -1569300\n"
     ]
    }
   ],
   "source": [
    "import numpy as n\n",
    "a=n.array([54,45,57,67,78,89])\n",
    "print(\"\\nAn Array:\",a)\n",
    "print(\"\\nSum:\",n.sum(a))\n",
    "print(\"Product\",n.prod(a))\n",
    "print(\"Mean:\",n.mean(a))\n",
    "print(\"Standard Deviation:\",n.std(a))\n",
    "print(\"Variance\",n.var(a))\n",
    "print(\"Minimum Value:\",n.min(a))\n",
    "print(\"Max:\",n.max(a))\n",
    "print(\"Min Index:\",n.argmin(a))\n",
    "print(\"Max Index:\",n.argmax(a))\n",
    "print(\"Median:\",n.median(a))\n",
    "print(\"Product:\",n.prod(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "436c517a-b08c-4823-bbe7-e398225a77ba",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
