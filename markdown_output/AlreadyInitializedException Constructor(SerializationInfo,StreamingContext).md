Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AlreadyInitializedException Constructor(SerializationInfo,StreamingContext)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [AlreadyInitializedException Class](topic2403.md) > [AlreadyInitializedException Constructor](topic2409.md) : AlreadyInitializedException Constructor(SerializationInfo,StreamingContext)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception being thrown

_context_
    The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or destination.

Glossary Item Box

Initializes a new instance of the [AlreadyInitializedException](topic2403.md) class with serialized data. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _info_ As SerializationInfo, _
       ByVal _context_ As StreamingContext _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim info As SerializationInfo
    Dim context As StreamingContext
     
    Dim instance As New [AlreadyInitializedException](topic2403.md)(info, context)  
  
C#|   
---|---  
      
    
    public AlreadyInitializedException( 
       SerializationInfo _info_ ,
       StreamingContext _context_
    )  
  
#### Parameters

 _info_
    The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception being thrown
 _context_
    The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or destination.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AlreadyInitializedException Class](topic2403.md)   
[AlreadyInitializedException Members](topic2404.md)   
[Overload List](topic2409.md)


