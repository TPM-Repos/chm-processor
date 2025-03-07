Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add(ControlData[],Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlCollection Class](topic7766.md) > [Add Method](topic7772.md) : Add(ControlData[],Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_deserialized_
    The deserialized control information, retrieved by using the [DriveWorks.Forms.DataModel.Serialization.ControlDeserializer](topic9604.md) class.

_renameDuplicates_
    True if duplicate controls should be renamed, false if an exception should be thrown instead.

Glossary Item Box

Takes the given deserialized control information, creates new controls, adds them to the collection, and returns them. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add( _
       ByVal _deserialized_() As [ControlData](topic9593.md), _
       ByVal _renameDuplicates_ As Boolean _
    ) As [ControlBase()](topic7698.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlCollection](topic7766.md)
    Dim deserialized() As [ControlData](topic9593.md)
    Dim renameDuplicates As Boolean
    Dim value() As [ControlBase](topic7698.md)
     
    value = instance.Add(deserialized, renameDuplicates)  
  
C#|   
---|---  
      
    
    public [ControlBase[]](topic7698.md) Add( 
       [ControlData](topic9593.md)[] _deserialized_ ,
       bool _renameDuplicates_
    )  
  
#### Parameters

 _deserialized_
    The deserialized control information, retrieved by using the [DriveWorks.Forms.DataModel.Serialization.ControlDeserializer](topic9604.md) class.
_renameDuplicates_
    True if duplicate controls should be renamed, false if an exception should be thrown instead.

#### Return Value

An array of the top-level controls that were added.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlCollection Class](topic7766.md)   
[ControlCollection Members](topic7767.md)   
[Overload List](topic7772.md)


