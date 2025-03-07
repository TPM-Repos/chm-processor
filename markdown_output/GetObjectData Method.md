Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetObjectData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [AzureCredentials Class](topic10646.md) : GetObjectData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    The System.Runtime.Serialization.SerializationInfo that will store data relating to this instance.

_context_
    The System.Runtime.Serialization.StreamingContext that contains contextual information about the source and destination.

Glossary Item Box

Sets the info with information about this instance. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub GetObjectData( _
       ByVal _info_ As SerializationInfo, _
       ByVal _context_ As StreamingContext _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [AzureCredentials](topic10646.md)
    Dim info As SerializationInfo
    Dim context As StreamingContext
     
    instance.GetObjectData(info, context)  
  
C#|   
---|---  
      
    
    public void GetObjectData( 
       SerializationInfo _info_ ,
       StreamingContext _context_
    )  
  
#### Parameters

 _info_
    The System.Runtime.Serialization.SerializationInfo that will store data relating to this instance.
_context_
    The System.Runtime.Serialization.StreamingContext that contains contextual information about the source and destination.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AzureCredentials Class](topic10646.md)   
[AzureCredentials Members](topic10647.md)


