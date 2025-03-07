Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NextStepIfFalseChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [DecisionNavigationStep Class](topic10125.md) : NextStepIfFalseChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the value of the [NextStepIfFalse](topic10140.md) property changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event NextStepIfFalseChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DecisionNavigationStep](topic10125.md)
    Dim handler As EventHandler
     
    AddHandler instance.NextStepIfFalseChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler NextStepIfFalseChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DecisionNavigationStep Class](topic10125.md)   
[DecisionNavigationStep Members](topic10126.md)


