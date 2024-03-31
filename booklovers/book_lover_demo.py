{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6cd691e4-1cc3-4228-8465-3343307c9d72",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from booklover import BookLover"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "85621a7d-f349-4c2c-a390-4b63f00fa4e6",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "newby = BookLover(\"Eric S. Arnold\", \"esa5ch@virginia.edu\", \"Comedy\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bc815a98-5eb2-4e37-a7fa-db8fe06378c1",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "newby.add_book(\"Dumb Dumb & Dumber\", 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5e8c800b-5c1a-404c-8189-a9f240f9095f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newby.num_books_read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "419aa023-78d1-4b7c-9f9e-74f1d5fd42de",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            book_name  book_rating\n",
      "0  Dumb Dumb & Dumber          4.0\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>book_name</th>\n",
       "      <th>book_rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Dumb Dumb &amp; Dumber</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            book_name  book_rating\n",
       "0  Dumb Dumb & Dumber          4.0"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newby.fav_books()"
   ]
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
