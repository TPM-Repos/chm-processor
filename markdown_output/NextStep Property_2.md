Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NextStep Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [NavigationStep Class](topic10175.md) : NextStep Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the navigation step to be activated after this. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Property NextStep As [NavigationStep](topic10175.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NavigationStep](topic10175.md)
    Dim value As [NavigationStep](topic10175.md)
     
    instance.NextStep = value
     
    value = instance.NextStep  
  
C#|   
---|---  
      
    
    public virtual [NavigationStep](topic10175.md) NextStep {get; set;}  
  
# Remarks

Changes to this property do not cause a cache update.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NavigationStep Class](topic10175.md)   
[NavigationStep Members](topic10176.md)


