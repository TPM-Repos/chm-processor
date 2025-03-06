![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CaptureViewAttribute Constructor(String,String,String,String,String,String)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13467.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [CaptureViewAttribute Class](topic13455.md) > [CaptureViewAttribute Constructor](topic13461.md) : CaptureViewAttribute Constructor(String,String,String,String,String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_invariantName_
    The invariant name used to identify this view.

_displayName_
    The name of the task pane to display in the UI.

_description_
    The description of this view.

_imageResourceUri_
    The resource uri of the icon to use for this view.

_insertAfter_
    (Optional) The name of the [ICaptureView](topic13347.md) to insert this view after. For a list of DriveWorks [ICaptureView](topic13347.md)s names see [DriveWorksCaptureViewNames](topic13545.md).

_insertBefore_
    (Optional) The name of the [ICaptureView](topic13347.md) to insert this view before. For a list of DriveWorks [ICaptureView](topic13347.md)s names see [DriveWorksCaptureViewNames](topic13545.md).

Glossary Item Box

Creates a new instance of the [CaptureViewAttribute](topic13455.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _invariantName_ As String, _
       ByVal _displayName_ As String, _
       ByVal _description_ As String, _
       ByVal _imageResourceUri_ As String, _
       ByVal _insertAfter_ As String, _
       ByVal _insertBefore_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim invariantName As String
    Dim displayName As String
    Dim description As String
    Dim imageResourceUri As String
    Dim insertAfter As String
    Dim insertBefore As String
     
    Dim instance As New [CaptureViewAttribute](topic13455.md)(invariantName, displayName, description, imageResourceUri, insertAfter, insertBefore)  
  
C#|   
---|---  
      
    
    public CaptureViewAttribute( 
       string _invariantName_ ,
       string _displayName_ ,
       string _description_ ,
       string _imageResourceUri_ ,
       string _insertAfter_ ,
       string _insertBefore_
    )  
  
#### Parameters

 _invariantName_
    The invariant name used to identify this view.
_displayName_
    The name of the task pane to display in the UI.
_description_
    The description of this view.
_imageResourceUri_
    The resource uri of the icon to use for this view.
_insertAfter_
    (Optional) The name of the [ICaptureView](topic13347.md) to insert this view after. For a list of DriveWorks [ICaptureView](topic13347.md)s names see [DriveWorksCaptureViewNames](topic13545.md).
_insertBefore_
    (Optional) The name of the [ICaptureView](topic13347.md) to insert this view before. For a list of DriveWorks [ICaptureView](topic13347.md)s names see [DriveWorksCaptureViewNames](topic13545.md).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CaptureViewAttribute Class](topic13455.md)   
[CaptureViewAttribute Members](topic13456.md)   
[Overload List](topic13461.md)

©2024 DriveWorks Ltd. All Rights Reserved.
