TaskAttribute Constructor(String,String,String)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskAttribute Class](topic11659.md) > [TaskAttribute Constructor](topic11665.md) : TaskAttribute Constructor(String,String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The localized display name of the task, or a resource string which identifies the string to use.

_image_
    A resource string which identifies the image to use.

_categoryName_
    The localized display name of the task's category, or a resource string which identifies the string to use.

Glossary Item Box

Initializes a new instance of the [TaskAttribute](topic11659.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _displayName_ As String, _
       ByVal _image_ As String, _
       ByVal _categoryName_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim displayName As String
    Dim image As String
    Dim categoryName As String
     
    Dim instance As New [TaskAttribute](topic11659.md)(displayName, image, categoryName)  
  
C#|   
---|---  
      
    
    public TaskAttribute( 
       string _displayName_ ,
       string _image_ ,
       string _categoryName_
    )  
  
#### Parameters

 _displayName_
    The localized display name of the task, or a resource string which identifies the string to use.
_image_
    A resource string which identifies the image to use.
_categoryName_
    The localized display name of the task's category, or a resource string which identifies the string to use.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskAttribute Class](topic11659.md)   
[TaskAttribute Members](topic11660.md)   
[Overload List](topic11665.md)


