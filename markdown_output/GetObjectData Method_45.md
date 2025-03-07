Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetObjectData Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [RequiredServiceException Class](topic915.md) : GetObjectData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception being thrown.

_context_
    The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or destination.

Glossary Item Box

Sets the info with information about the instance. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Sub GetObjectData( _
       ByVal _info_ As SerializationInfo, _
       ByVal _context_ As StreamingContext _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RequiredServiceException](topic915.md)
    Dim info As SerializationInfo
    Dim context As StreamingContext
     
    instance.GetObjectData(info, context)  
  
C#|   
---|---  
      
    
    public override void GetObjectData( 
       SerializationInfo _info_ ,
       StreamingContext _context_
    )  
  
#### Parameters

 _info_
    The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception being thrown.
_context_
    The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or destination.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RequiredServiceException Class](topic915.md)   
[RequiredServiceException Members](topic916.md)


