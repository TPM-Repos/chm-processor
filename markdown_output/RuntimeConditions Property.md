       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuntimeConditions Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTask Class](topic6407.md) : RuntimeConditions Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the collection of conditions that will be released alongside the component and evaluated at run time. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property RuntimeConditions As [ComponentTaskConditions](topic6561.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTask](topic6407.md)
    Dim value As [ComponentTaskConditions](topic6561.md)
     
    value = instance.RuntimeConditions  
  
C#|   
---|---  
      
    
    public [ComponentTaskConditions](topic6561.md) RuntimeConditions {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTask Class](topic6407.md)   
[ComponentTask Members](topic6408.md)


