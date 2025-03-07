Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MarkFailed Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : MarkFailed Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The unique identifier of the component.

_failedCount_
    The total number of times the component has failed to be generated.

Glossary Item Box

Marks the specified component as having failed the given number of times. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub MarkFailed( _
       ByVal _componentId_ As Guid, _
       ByVal _failedCount_ As Integer _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
    Dim failedCount As Integer
     
    instance.MarkFailed(componentId, failedCount)  
  
C#|   
---|---  
      
    
    public void MarkFailed( 
       Guid _componentId_ ,
       int _failedCount_
    )  
  
#### Parameters

 _componentId_
    The unique identifier of the component.
_failedCount_
    The total number of times the component has failed to be generated.

# Remarks

The failedCount must be at least one (1).

Marking a component as having failed automatically clears the generating and generated fields.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


