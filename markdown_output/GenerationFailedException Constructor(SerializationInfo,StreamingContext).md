Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerationFailedException Constructor(SerializationInfo,StreamingContext)   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [GenerationFailedException Class](topic15228.md) > [GenerationFailedException Constructor](topic15234.md) : GenerationFailedException Constructor(SerializationInfo,StreamingContext)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    The serialized object data.

_context_
    The streaming context.

Glossary Item Box

Deserializes an instance of the [GenerationFailedException](topic15228.md) class. 

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
     
    Dim instance As New [GenerationFailedException](topic15228.md)(info, context)  
  
C#|   
---|---  
      
    
    protected GenerationFailedException( 
       SerializationInfo _info_ ,
       StreamingContext _context_
    )  
  
#### Parameters

 _info_
    The serialized object data.
_context_
    The streaming context.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationFailedException Class](topic15228.md)   
[GenerationFailedException Members](topic15229.md)   
[Overload List](topic15234.md)


