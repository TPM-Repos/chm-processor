Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FailedOutput Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeWithStatus Class](topic6990.md) : FailedOutput Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the end point that allows logical navigation connections to be made from this node when this node fails during execution. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property FailedOutput As [NodeNavigationOutput](topic7067.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeWithStatus](topic6990.md)
    Dim value As [NodeNavigationOutput](topic7067.md)
     
    value = instance.FailedOutput  
  
C#|   
---|---  
      
    
    public [NodeNavigationOutput](topic7067.md) FailedOutput {get;}  
  
# Remarks

This end point can be mapped to a [NodeNavigationInput](topic7058.md) to set up the order in which the nodes will execute.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExecutableNodeWithStatus Class](topic6990.md)   
[ExecutableNodeWithStatus Members](topic6991.md)


