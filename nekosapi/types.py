from enum import Enum


class VerificationStatus(Enum):
    """
    An image's verification status. Since images uploaded to the API are
    manually verified by content moderators, this status tells you wether the
    content moderators have seen and reviewed this image or not and the result
    of that review.

    The four statuses are:
    - `NOT_REVIEWED`: This image has not yet been reviewed by a content
      moderator.
    - `ON_REVIEW`: The image has been seen by a content moderator, but it is
      still pending a definitive review. You might see this status when images
      are being considered because the style does not completely match the
      API's art style or the "age rating" is still being discussed.
    - `DECLINED`: The image does not meet the requirements to be served by the
      API. Content moderators have thousands of images to verify so they cannot
      provide an explanation on why the image has been declined.
    - `VERIFIED`: The image has been reviewed by a content moderator and was
      accepted in the API. These images can be seen by anyone.
    """
    
    NOT_REVIEWED = 'not_reviewed'
    ON_REVIEW = 'on_review'
    VERIFIED = 'verified'
    DECLINED = 'declined'


class AgeRating(Enum):
    """
    This "age rating" is not a real age rating since it does not specify any
    kind of minimum age to see an image. It provides information about the
    "hentainess" of the image.

    Mainly, the age ratings mean the following:
    - `SAFE_FOR_WORK`: The image has not the slightest bit of suggestive content.
    - `QUESTIONABLE`: Still safe for work, but they contain typical content you'd
      see in a fan-service anime episode. Girls in bikinies are an example of
      questionable content.
    - `SUGGESTIVE`: Although the image has no kind of explicit content, it
      is, as the name says, suggestive. In other words, light ecchi.
    - `BORDERLINE`: These images contain highly suggestive content. Few clothing,
      uncovered parts of the body, etc. There is no sensitive/explicit content
      but it is not recommended to see this in public. Minors should also avoid
      seeing this content.
    - `EXPLICIT`: In other words, hentai. As the name says, explicit content is
      shown in this kind of images. Minors must not see images marked as
      `EXPLICIT`.
    
    Take into account that content like gore is not taken into account in this
    "age rating". To exclude that kind of content, you'll need to use filters.
    """

    SAFE_FOR_WORK = 'sfw'
    QUESTIONABLE = 'questionable'
    SUGGESTIVE = 'suggestive'
    BORDERLINE = 'borderline'
    EXPLICIT = 'explicit'
