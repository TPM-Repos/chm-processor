Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
References Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [CapturedComponentInfo Class](topic6154.md) : References Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an array of identifiers of components referenced as children of the component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property References As Guid()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedComponentInfo](topic6154.md)
    Dim value() As Guid
     
    value = instance.References  
  
C#|   
---|---  
      
    
    public Guid[] References {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedComponentInfo Class](topic6154.md)   
[CapturedComponentInfo Members](topic6155.md)


