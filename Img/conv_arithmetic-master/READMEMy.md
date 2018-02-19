# Convolution animations
Image courtesy of [ Vincent Dumoulin, Francesco Visin. A guide to convolution arithmetic for deep learning]("https://github.com/vdumoulin/conv_arithmetic")

__N.B.: Blue maps are inputs, and cyan maps are outputs.__

<table style="width:100%; table-layout:fixed;">
  <tr>
    <td><img width="150px" src="gif/no_padding_no_strides.gif"></td>
    <td><img width="150px" src="gif/arbitrary_padding_no_strides.gif"></td>
    <td><img width="150px" src="gif/same_padding_no_strides.gif"></td>
    <td><img width="150px" src="gif/full_padding_no_strides.gif"></td>
  </tr>
  <tr>
    <td>No padding, no strides</td>
    <td>Arbitrary padding, no strides</td>
    <td>Half padding, no strides</td>
    <td>Full padding, no strides</td>
  </tr>
  <tr>
    <td><img width="150px" src="gif/no_padding_strides.gif"></td>
    <td><img width="150px" src="gif/padding_strides.gif"></td>
    <td><img width="150px" src="gif/padding_strides_odd.gif"></td>
    <td></td>
  </tr>
  <tr>
    <td>No padding, strides</td>
    <td>Padding, strides</td>
    <td>Padding, strides (odd)</td>
    <td></td>
  </tr>
</table>

# Transposed convolution animations

__N.B.: Blue maps are inputs, and cyan maps are outputs.__

<table style="width:100%; table-layout:fixed;">
  <tr>
    <td><img width="150px" src="gif/no_padding_no_strides_transposed.gif"></td>
    <td><img width="150px" src="gif/arbitrary_padding_no_strides_transposed.gif"></td>
    <td><img width="150px" src="gif/same_padding_no_strides_transposed.gif"></td>
    <td><img width="150px" src="gif/full_padding_no_strides_transposed.gif"></td>
  </tr>
  <tr>
    <td>No padding, no strides, transposed</td>
    <td>Arbitrary padding, no strides, transposed</td>
    <td>Half padding, no strides, transposed</td>
    <td>Full padding, no strides, transposed</td>
  </tr>
  <tr>
    <td><img width="150px" src="gif/no_padding_strides_transposed.gif"></td>
    <td><img width="150px" src="gif/padding_strides_transposed.gif"></td>
    <td><img width="150px" src="gif/padding_strides_odd_transposed.gif"></td>
    <td></td>
  </tr>
  <tr>
    <td>No padding, strides, transposed</td>
    <td>Padding, strides, transposed</td>
    <td>Padding, strides, transposed (odd)</td>
    <td></td>
  </tr>
</table>

# Dilated convolution animations

__N.B.: Blue maps are inputs, and cyan maps are outputs.__

<table style="width:25%"; table-layout:fixed;>
  <tr>
    <td><img width="150px" src="gif/dilation.gif"></td>
  </tr>
  <tr>
    <td>No padding, no stride, dilation</td>
  </tr>
</table>
