Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NavigationOutput Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Task Class](topic11629.md) : NavigationOutput Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the end point that allows logical navigation connections to be made from this task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides ReadOnly Property NavigationOutput As [NodeNavigationOutput](topic7067.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Task](topic11629.md)
    Dim value As [NodeNavigationOutput](topic7067.md)
     
    value = instance.NavigationOutput  
  
C#|   
---|---  
      
    
    public override [NodeNavigationOutput](topic7067.md) NavigationOutput {get;}  
  
# Remarks

This end point can be mapped to a [DriveWorks.EventFlow.NodeNavigationInput](topic7058.md) to set up the order in which the tasks will execute.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Task Class](topic11629.md)   
[Task Members](topic11630.md)


