Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviousMacroRuleChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [NavigationStep Class](topic10175.md) : PreviousMacroRuleChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the rule, which determines the macro to be fired when the previous step is activated, changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event PreviousMacroRuleChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NavigationStep](topic10175.md)
    Dim handler As EventHandler
     
    AddHandler instance.PreviousMacroRuleChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler PreviousMacroRuleChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NavigationStep Class](topic10175.md)   
[NavigationStep Members](topic10176.md)


