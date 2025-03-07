Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyEvaluatedAsInvalidName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyEvaluatedAsInvalidName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_nameResult_
    The result of the name rule.

Glossary Item Box

Called when the current component is determined to have an invalid name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyEvaluatedAsInvalidName( _
       ByVal _nameResult_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim nameResult As String
     
    instance.NotifyEvaluatedAsInvalidName(nameResult)  
  
C#|   
---|---  
      
    
    void NotifyEvaluatedAsInvalidName( 
       string _nameResult_
    )  
  
#### Parameters

 _nameResult_
    The result of the name rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


