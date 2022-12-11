import axios from "axios"
import React from "react"
import AnalyzeNav from "./components/AnalyzeNav";
import { useState } from "react";
import "./Home.css"

export default function Analyze2(props) {
    const baseURL = "http://127.0.0.1:8000/api"
    const [num, setNum] = useState('');
    const [submit, toggleSubmit] = useState(false);
    let JsonData = ""
    const [arr, setdatarry] = useState([]);
    let jsonarray = [];

    const handleNumChange = (event) => {
        setNum(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const res = await axios.get(`${baseURL}/mapreduce/?dataSet=restaurants&top_review_num=${num}`)
            jsonarray = res.data.res
            let newarr = []
            for (let i = 0; i < jsonarray.length; i++) {
                newarr.push({
                    id: newarr.length,
                    city: jsonarray[i].city,
                    name: jsonarray[i].name,
                    rate: jsonarray[i].rate,
                    reviewCount: jsonarray[i].review_cnt,
                })
            }
            setdatarry(newarr)
            toggleSubmit(true)
        } catch (err) {
            console.error(err)
        }
    }

    const DisplayData = arr.map((info) => {
        return (
            <tr>
                <td>{info.city}</td>
                <td>{info.name}</td>
                <td>{info.rate}</td>
                <td>{info.reviewCount}</td>
            </tr>
        )
    }
    )

    return (
        <div className="App">
            <AnalyzeNav />
            <form className="iform" onSubmit={e => handleSubmit(e)}>
                <label htmlFor="num">I want to select the top</label>
                <input
                    type="number"
                    id="num"
                    name="num"
                    value={num}
                    onChange={handleNumChange}
                />
                <span>review count restaurants</span>
                <br />
                <button className="button" type="submit">Submit</button>
            </form>
            <br />
            {
                submit && <div className="result table">
                    <table className="table table-striped">
                        <thead>
                            <tr>
                                <th>City</th>
                                <th>Restaurant Name</th>
                                <th>Rate</th>
                                <th>Number of Reviews</th>
                            </tr>
                        </thead>
                        <tbody>
                            {DisplayData}
                        </tbody>
                    </table>

                </div>
            }
        </div>
    );
}