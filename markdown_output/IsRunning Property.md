Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsRunning Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : IsRunning Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Determines whether the specification is running. See remarks for details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property IsRunning As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As Boolean
     
    value = instance.IsRunning  
  
C#|   
---|---  
      
    
    public bool IsRunning {get;}  
  
# Remarks

The IsRunning property determines whether a design master is active for the specification which may be true even if the current state of the specification isn't a running state, for example, during paused to paused state transitions or during operations where a condition or task requires access to a design master.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


