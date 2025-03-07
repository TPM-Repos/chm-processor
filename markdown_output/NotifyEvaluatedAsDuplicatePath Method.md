Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyEvaluatedAsDuplicatePath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyEvaluatedAsDuplicatePath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fullPath_
    The evaluated path to the new component.

Glossary Item Box

Called when the current component is determined to have the same path as an existing component, but a different target name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyEvaluatedAsDuplicatePath( _
       ByVal _fullPath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim fullPath As String
     
    instance.NotifyEvaluatedAsDuplicatePath(fullPath)  
  
C#|   
---|---  
      
    
    void NotifyEvaluatedAsDuplicatePath( 
       string _fullPath_
    )  
  
#### Parameters

 _fullPath_
    The evaluated path to the new component.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


