Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyEvaluatedAsNewComponentWithInvalidPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyEvaluatedAsNewComponentWithInvalidPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_invalidPath_
    The path which was generated.

Glossary Item Box

Called when the current component is determined to have an invalid full path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyEvaluatedAsNewComponentWithInvalidPath( _
       ByVal _invalidPath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim invalidPath As String
     
    instance.NotifyEvaluatedAsNewComponentWithInvalidPath(invalidPath)  
  
C#|   
---|---  
      
    
    void NotifyEvaluatedAsNewComponentWithInvalidPath( 
       string _invalidPath_
    )  
  
#### Parameters

 _invalidPath_
    The path which was generated.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


