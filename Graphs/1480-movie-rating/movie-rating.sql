-- Query for the user with the most movie ratings
(SELECT U.name AS results
FROM Users U
JOIN (
    SELECT user_id, COUNT(*) AS num_ratings
    FROM MovieRating
    GROUP BY user_id
) AS RatingCounts ON U.user_id = RatingCounts.user_id
ORDER BY RatingCounts.num_ratings DESC, U.name ASC
LIMIT 1)

UNION ALL

-- Query for the movie with the highest average rating in February 2020
(SELECT  M.title AS results
FROM Movies M
JOIN (
    SELECT movie_id, AVG(rating) AS avg_rating
    FROM MovieRating
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY movie_id
) AS MovieAverages ON M.movie_id = MovieAverages.movie_id
ORDER BY MovieAverages.avg_rating DESC, M.title ASC
LIMIT 1);
