Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnNextMacroRule Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [NavigationStep Class](topic10175.md) : OnNextMacroRule Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the rule which defines the name of the macro to be executed when the next step is activated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property OnNextMacroRule As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NavigationStep](topic10175.md)
    Dim value As String
     
    instance.OnNextMacroRule = value
     
    value = instance.OnNextMacroRule  
  
C#|   
---|---  
      
    
    public string OnNextMacroRule {get; set;}  
  
# Remarks

Changes to this property cause a cache update.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NavigationStep Class](topic10175.md)   
[NavigationStep Members](topic10176.md)


