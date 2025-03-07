Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateDecision Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) : CreateDecision Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the new decision.

Glossary Item Box

Creates a new decision. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function CreateDecision( _
       ByVal _name_ As String _
    ) As [DecisionNavigationStep](topic10125.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim name As String
    Dim value As [DecisionNavigationStep](topic10125.md)
     
    value = instance.CreateDecision(name)  
  
C#|   
---|---  
      
    
    public abstract [DecisionNavigationStep](topic10125.md) CreateDecision( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the new decision.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)


