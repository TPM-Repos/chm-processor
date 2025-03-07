Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CaptureViewAttribute Constructor(String,String,String,String)   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [CaptureViewAttribute Class](topic13455.md) > [CaptureViewAttribute Constructor](topic13461.md) : CaptureViewAttribute Constructor(String,String,String,String)  
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

Glossary Item Box

Creates a new instance of the [CaptureViewAttribute](topic13455.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _invariantName_ As String, _
       ByVal _displayName_ As String, _
       ByVal _description_ As String, _
       ByVal _imageResourceUri_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim invariantName As String
    Dim displayName As String
    Dim description As String
    Dim imageResourceUri As String
     
    Dim instance As New [CaptureViewAttribute](topic13455.md)(invariantName, displayName, description, imageResourceUri)  
  
C#|   
---|---  
      
    
    public CaptureViewAttribute( 
       string _invariantName_ ,
       string _displayName_ ,
       string _description_ ,
       string _imageResourceUri_
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CaptureViewAttribute Class](topic13455.md)   
[CaptureViewAttribute Members](topic13456.md)   
[Overload List](topic13461.md)


