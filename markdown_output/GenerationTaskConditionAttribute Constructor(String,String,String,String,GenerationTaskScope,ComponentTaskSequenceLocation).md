![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerationTaskConditionAttribute Constructor(String,String,String,String,GenerationTaskScope,ComponentTaskSequenceLocation)   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [GenerationTaskConditionAttribute Class](topic13721.md) > [GenerationTaskConditionAttribute Constructor](topic13727.md) : GenerationTaskConditionAttribute Constructor(String,String,String,String,GenerationTaskScope,ComponentTaskSequenceLocation)  
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

_locations_
    The allowed locations this condition can execute in.

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
       ByVal _locations_ As [ComponentTaskSequenceLocation](topic6406.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim name As String
    Dim description As String
    Dim image As String
    Dim category As String
    Dim scope As [GenerationTaskScope](topic13452.md)
    Dim locations As [ComponentTaskSequenceLocation](topic6406.md)
     
    Dim instance As New [GenerationTaskConditionAttribute](topic13721.md)(name, description, image, category, scope, locations)  
  
C#|   
---|---  
      
    
    public GenerationTaskConditionAttribute( 
       string _name_ ,
       string _description_ ,
       string _image_ ,
       string _category_ ,
       [GenerationTaskScope](topic13452.md) _scope_ ,
       [ComponentTaskSequenceLocation](topic6406.md) _locations_
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
_locations_
    The allowed locations this condition can execute in.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GenerationTaskConditionAttribute Class](topic13721.md)   
[GenerationTaskConditionAttribute Members](topic13722.md)   
[Overload List](topic13727.md)


