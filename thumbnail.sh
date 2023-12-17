# this script works only on OS X
# as soon as our backend is complete, it will have python thumbnail util for the uploaded photos
#
#
# create thumbnails dir if it isn't there yet
mkdir -p thumbnails

# go through each jpg/JPG in animals directory
for img in animals/*.{jpg,JPG}; do
  # resize it to be not bigger than 600px and put into thumbnails dir under the same filename
  sips -Z 600 "$img" --out "thumbnails/$(basename "$img")"
done
