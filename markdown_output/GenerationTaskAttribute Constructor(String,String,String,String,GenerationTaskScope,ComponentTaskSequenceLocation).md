![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerationTaskAttribute Constructor(String,String,String,String,GenerationTaskScope,ComponentTaskSequenceLocation)   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [GenerationTaskAttribute Class](topic13693.md) > [GenerationTaskAttribute Constructor](topic13699.md) : GenerationTaskAttribute Constructor(String,String,String,String,GenerationTaskScope,ComponentTaskSequenceLocation)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The title to show the user when administrating the task.

_description_
    The description providing the user with additional information about this task.

_image_
    The resource uri to the image used to represent the associated task.

_category_
    The category of the task.

_scope_
    Specifies with type of components this task supports.

_allowedLocations_
    The sequence locations this task is allowed to be executed inside of.

Glossary Item Box

Creates a new instance of the see [DriveWorks.Components.Tasks.ComponentTaskAttribute](topic6455.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _name_ As String, _
       ByVal _description_ As String, _
       ByVal _image_ As String, _
       ByVal _category_ As String, _
       ByVal _scope_ As [GenerationTaskScope](topic13452.md), _
       ByVal _allowedLocations_ As [ComponentTaskSequenceLocation](topic6406.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim name As String
    Dim description As String
    Dim image As String
    Dim category As String
    Dim scope As [GenerationTaskScope](topic13452.md)
    Dim allowedLocations As [ComponentTaskSequenceLocation](topic6406.md)
     
    Dim instance As New [GenerationTaskAttribute](topic13693.md)(name, description, image, category, scope, allowedLocations)  
  
C#|   
---|---  
      
    
    public GenerationTaskAttribute( 
       string _name_ ,
       string _description_ ,
       string _image_ ,
       string _category_ ,
       [GenerationTaskScope](topic13452.md) _scope_ ,
       [ComponentTaskSequenceLocation](topic6406.md) _allowedLocations_
    )  
  
#### Parameters

 _name_
    The title to show the user when administrating the task.
_description_
    The description providing the user with additional information about this task.
_image_
    The resource uri to the image used to represent the associated task.
_category_
    The category of the task.
_scope_
    Specifies with type of components this task supports.
_allowedLocations_
    The sequence locations this task is allowed to be executed inside of.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GenerationTaskAttribute Class](topic13693.md)   
[GenerationTaskAttribute Members](topic13694.md)   
[Overload List](topic13699.md)


