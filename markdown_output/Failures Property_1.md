Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Failures Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TriggeredActionDetails Class](topic5724.md) : Failures Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the failures from any attempts made to run the triggered action. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Failures As [DeferredTaskFailureDetails()](topic2666.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TriggeredActionDetails](topic5724.md)
    Dim value() As [DeferredTaskFailureDetails](topic2666.md)
     
    value = instance.Failures  
  
C#|   
---|---  
      
    
    public [DeferredTaskFailureDetails[]](topic2666.md) Failures {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TriggeredActionDetails Class](topic5724.md)   
[TriggeredActionDetails Members](topic5725.md)


