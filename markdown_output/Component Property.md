Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Component Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [RegenerateAndDeleteComponentTask Class](topic12426.md) : Component Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the component that'll be marked for generation and have its generated file deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Component As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RegenerateAndDeleteComponentTask](topic12426.md)
    Dim value As String
     
    instance.Component = value
     
    value = instance.Component  
  
C#|   
---|---  
      
    
    public string Component {get; set;}  
  
# Remarks

This value is either the Globally Unique Identifier (GUID) or the Target Path of a released component.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RegenerateAndDeleteComponentTask Class](topic12426.md)   
[RegenerateAndDeleteComponentTask Members](topic12427.md)


