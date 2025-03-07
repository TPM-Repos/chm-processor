Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NavigationOutput Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Condition Class](topic10804.md) : NavigationOutput Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the navigation output of this node. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides ReadOnly Property NavigationOutput As [NodeNavigationOutput](topic7067.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Condition](topic10804.md)
    Dim value As [NodeNavigationOutput](topic7067.md)
     
    value = instance.NavigationOutput  
  
C#|   
---|---  
      
    
    public override [NodeNavigationOutput](topic7067.md) NavigationOutput {get;}  
  
# Remarks

Warning: Connecting another [DriveWorks.EventFlow.IFlowNode](topic6873.md) to this output bypasses the validation of the condition.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Condition Class](topic10804.md)   
[Condition Members](topic10805.md)


