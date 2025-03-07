Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyEvaluatedAsNewComponent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyEvaluatedAsNewComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fullPath_
    The path which was generated.

Glossary Item Box

Called when the current component is determined to be a new component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyEvaluatedAsNewComponent( _
       ByVal _fullPath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim fullPath As String
     
    instance.NotifyEvaluatedAsNewComponent(fullPath)  
  
C#|   
---|---  
      
    
    void NotifyEvaluatedAsNewComponent( 
       string _fullPath_
    )  
  
#### Parameters

 _fullPath_
    The path which was generated.

# Remarks

The unique identifier assigned to the new component is the same as the component tracking identifier provided to the [NotifyBeginEvaluate](topic6125.md) method.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


