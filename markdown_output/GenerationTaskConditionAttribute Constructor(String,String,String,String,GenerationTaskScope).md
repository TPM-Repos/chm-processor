Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerationTaskConditionAttribute Constructor(String,String,String,String,GenerationTaskScope)   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [GenerationTaskConditionAttribute Class](topic13721.md) > [GenerationTaskConditionAttribute Constructor](topic13727.md) : GenerationTaskConditionAttribute Constructor(String,String,String,String,GenerationTaskScope)  
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

Glossary Item Box

Creates a new instance of the see [DriveWorks.Components.Tasks.ComponentTaskAttribute](topic6455.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _name_ As String, _
       ByVal _description_ As String, _
       ByVal _image_ As String, _
       ByVal _category_ As String, _
       ByVal _scope_ As [GenerationTaskScope](topic13452.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim name As String
    Dim description As String
    Dim image As String
    Dim category As String
    Dim scope As [GenerationTaskScope](topic13452.md)
     
    Dim instance As New [GenerationTaskConditionAttribute](topic13721.md)(name, description, image, category, scope)  
  
C#|   
---|---  
      
    
    public GenerationTaskConditionAttribute( 
       string _name_ ,
       string _description_ ,
       string _image_ ,
       string _category_ ,
       [GenerationTaskScope](topic13452.md) _scope_
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationTaskConditionAttribute Class](topic13721.md)   
[GenerationTaskConditionAttribute Members](topic13722.md)   
[Overload List](topic13727.md)


