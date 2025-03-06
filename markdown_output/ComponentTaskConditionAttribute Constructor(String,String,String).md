![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTaskConditionAttribute Constructor(String,String,String)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6521.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskConditionAttribute Class](topic6512.md) > [ComponentTaskConditionAttribute Constructor](topic6518.md) : ComponentTaskConditionAttribute Constructor(String,String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title to show the user when administrating the condition.

_description_
    The description providing the user with additional information about this condition.

_image_
    The resource uri to the image used to represent the associated condition.

Glossary Item Box

Creates a new instance of the see [ComponentTaskAttribute](topic6455.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _title_ As String, _
       ByVal _description_ As String, _
       ByVal _image_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim title As String
    Dim description As String
    Dim image As String
     
    Dim instance As New [ComponentTaskConditionAttribute](topic6512.md)(title, description, image)  
  
C#|   
---|---  
      
    
    public ComponentTaskConditionAttribute( 
       string _title_ ,
       string _description_ ,
       string _image_
    )  
  
#### Parameters

 _title_
    The title to show the user when administrating the condition.
_description_
    The description providing the user with additional information about this condition.
_image_
    The resource uri to the image used to represent the associated condition.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskConditionAttribute Class](topic6512.md)   
[ComponentTaskConditionAttribute Members](topic6513.md)   
[Overload List](topic6518.md)

©2024 DriveWorks Ltd. All Rights Reserved.
