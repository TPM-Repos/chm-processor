Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Properties Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel.Serialization Namespace](topic9591.md) > [ControlData Class](topic9593.md) : Properties Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Information about the data assigned to properties of the instantiated control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Properties As [PropertyData()](topic9611.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlData](topic9593.md)
    Dim value() As [PropertyData](topic9611.md)
     
    instance.Properties = value
     
    value = instance.Properties  
  
C#|   
---|---  
      
    
    public [PropertyData[]](topic9611.md) Properties {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlData Class](topic9593.md)   
[ControlData Members](topic9594.md)


