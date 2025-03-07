Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NextStep Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [FinishNavigationStep Class](topic10145.md) : NextStep Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Overridden to throw an exception if it is attempted to change the next step as the Finish step cannot have a next step. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides NotOverridable Property NextStep As [NavigationStep](topic10175.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FinishNavigationStep](topic10145.md)
    Dim value As [NavigationStep](topic10175.md)
     
    instance.NextStep = value
     
    value = instance.NextStep  
  
C#|   
---|---  
      
    
    public override [NavigationStep](topic10175.md) NextStep {get; set;}  
  
# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| Thrown if it is attempted to modify the property's value.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FinishNavigationStep Class](topic10145.md)   
[FinishNavigationStep Members](topic10146.md)


