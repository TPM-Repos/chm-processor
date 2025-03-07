Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DesignMasterReadOnlyException Constructor(SerializationInfo,StreamingContext)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [DesignMasterReadOnlyException Class](topic2695.md) > [DesignMasterReadOnlyException Constructor](topic2701.md) : DesignMasterReadOnlyException Constructor(SerializationInfo,StreamingContext)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about the exception being thrown

_context_
    The System.Runtime.Serialization.StreamingContext that contains contextual information about the source or destination.

Glossary Item Box

Initializes a new instance of the [ItemNotFoundException](topic3571.md) class with serialized data. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Function New( _
       ByVal _info_ As SerializationInfo, _
       ByVal _context_ As StreamingContext _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim info As SerializationInfo
    Dim context As StreamingContext
     
    Dim instance As New [DesignMasterReadOnlyException](topic2695.md)(info, context)  
  
C#|   
---|---  
      
    
    protected DesignMasterReadOnlyException( 
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

[DesignMasterReadOnlyException Class](topic2695.md)   
[DesignMasterReadOnlyException Members](topic2696.md)   
[Overload List](topic2701.md)


